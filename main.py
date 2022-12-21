from turtle import Screen
from snake import Snake
import time

# screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")


snake = Snake()
screen.update()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


gameover = False
while not gameover:
    snake.move()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()