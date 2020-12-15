# Code for Day 20 Project

from turtle import Screen
from snake import Snake
import time

# Create Snake
snake = Snake()

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
game = True

while game:

    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
