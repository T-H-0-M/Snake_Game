from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for x in range(3):
            self.snake.append(Turtle(shape="square"))
            self.snake[x].color("white")
            self.snake[x].penup()
            self.snake[x].setpos(-(x * 20), 0)

    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[x - 1].xcor()
            new_y = self.snake[x - 1].ycor()
            self.snake[x].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
