# Code for Day 21 Project

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create Snake, Food and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Create and configure Screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.update()

# Configure Screen to listen for key taps
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Game code
while True:

    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if abs(snake.head.xcor()) > 295 or abs(snake.head.ycor()) > 295:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
