"""
snake.py: A module containing the Snake class for the Snake game.

The Snake class represents the snake in the Snake game. It provides methods for creating the initial snake, moving the
snake, extending the snake, resetting the snake, and changing the direction of the snake.

"""

from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """
    A class representing the snake in the Snake game.

    Attributes:
        - snake (list): A list of turtle objects representing the segments of the snake.
        - head (Turtle): The turtle object representing the head of the snake.

    Methods:
        - __init__(): Initializes a new instance of the Snake class.
        - create_snake(): Creates the initial segments of the snake.
        - move(): Moves the snake forward.
        - add_segment(position): Adds a new segment to the snake at the specified position.
        - extend(): Extends the snake by adding a new segment at the end.
        - reset_snake(): Resets the snake to its initial state.
        - up(): Changes the direction of the snake to up.
        - down(): Changes the direction of the snake to down.
        - right(): Changes the direction of the snake to right.
        - left(): Changes the direction of the snake to left.

    """

    def __init__(self):
        """
        Initializes a new instance of the Snake class.

        Creates the initial segments of the snake and sets the head of the snake.

        """
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """
        Creates the initial segments of the snake.

        Adds three segments to the snake at the predefined starting positions.

        """
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def move(self):
        """
        Moves the snake forward.

        Moves each segment of the snake forward by a fixed distance. The movement is achieved by updating the positions of
        the segments based on the position of the previous segment.

        """
        for x in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[x - 1].xcor()
            new_y = self.snake[x - 1].ycor()
            self.snake[x].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.

        Args:
            - position (tuple): The x and y coordinates of the new segment.

        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.snake.append(new_segment)

    def extend(self):
        """
        Extends the snake by adding a new segment at the end.

        Uses the add_segment method to add a new segment to the snake at the position of the last segment.

        """
        self.add_segment(self.snake[-1].position())

    def reset_snake(self):
        """
        Resets the snake to its initial state.

        Clears the positions of all segments, clears the snake list, recreates the initial segments, and sets the head of
        the snake.

        """
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        """
        Changes the direction of the snake to up.

        Changes the heading of the head of the snake to UP (90 degrees) if the current heading is not DOWN (270 degrees).

        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the direction of the snake to down.

        Changes the heading of the head of the snake to DOWN (270 degrees) if the current heading is not UP (90 degrees).

        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """
        Changes the direction of the snake to right.

        Changes the heading of the head of the snake to RIGHT (0 degrees) if the current heading is not LEFT (180 degrees).

        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """
        Changes the direction of the snake to left.

        Changes the heading of the head of the snake to LEFT (180 degrees) if the current heading is not RIGHT (0 degrees).

        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
