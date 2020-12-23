# Class for code of Day 22 Project

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position_coords):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position_coords)

    def go_up(self):
        """ Moves up the paddle. """
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        """ Moves down the paddle. """
        self.goto(self.xcor(), self.ycor() - 20)
