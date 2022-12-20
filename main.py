from turtle import Screen, Turtle

# screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# generating the beginning of the snake
snake = []
for x in range(3):
    snake.append(Turtle(shape="square"))
    snake[x].color("white")
    snake[x].setpos(-(x*20), 0)

screen.exitonclick()