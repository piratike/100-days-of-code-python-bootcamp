# Code for Day 22 Project

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the paddles, the ball and the scoreboard
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Create and configure Screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Configure Screen to listen for key taps
screen.listen()
screen.onkey(rpaddle.go_up, 'Up')
screen.onkey(rpaddle.go_down, 'Down')
screen.onkey(lpaddle.go_up, 'w')
screen.onkey(lpaddle.go_down, 's')

game = True

while game:

    time.sleep(0.03)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
