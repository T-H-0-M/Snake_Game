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
count = 0
game_over = False
while not game_over:
    snake.move()
    time.sleep(1)
    screen.update()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True

    # Detect collision with tail

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10 and count > 2:
            game_over = True
        print(count)
        count += 1

score.gameover()
screen.exitonclick()
