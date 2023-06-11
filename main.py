"""
main.py: The main module for running the Snake game.

This module sets up the game screen, initializes the snake, food, and scoreboard objects, and implements the game logic
and event listeners for controlling the snake's movement.

"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_DIMENSIONS = (600, 600)

# Declaring all objects
screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

# Screen configuration
screen.setup(height=SCREEN_DIMENSIONS[0], width=SCREEN_DIMENSIONS[1])
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

# Drawing boarder
score.draw_border(x=(SCREEN_DIMENSIONS[0]/2), y=(SCREEN_DIMENSIONS[1]/2))

# Screen event listener declarations for snake movement
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Main game loop
game_over = False
while not game_over:
    time.sleep(0.1)
    snake.move()
    screen.update()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
