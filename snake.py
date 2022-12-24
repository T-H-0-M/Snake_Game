from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = {(0, 0), (-20, 0), (-40, 0)}


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # Creates the first three segments of the snake
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    # Moves all segments forward by 20 spaces
    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[x - 1].xcor()
            new_y = self.snake[x - 1].ycor()
            self.snake[x].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Adds 1 segment to the snake at the parsed position
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.snake.append(new_segment)

    # adds a new segment to the snake using the add_segment method
    def extend(self):
        self.add_segment(self.snake[-1].position())

    # Following methods set the head of the snake to a specific orientation.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
