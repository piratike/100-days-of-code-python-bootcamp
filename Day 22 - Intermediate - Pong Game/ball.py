# Class for code of Day 22 Project

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.moving_speed = 0.1

    def move(self):
        """ Moves the ball across the screen. """

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Makes the ball bounce in Y axis. """

        self.y_move *= -1

    def bounce_x(self):
        """ Makes the ball bounce in X axis. """

        self.x_move *= -1
        self.moving_speed *= 0.9

    def reset_position(self):
        """ Returns the ball to (0, 0). """

        self.goto(0, 0)
        self.moving_speed = 0.1
        self.bounce_x()
