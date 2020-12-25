# Class for code of Day 20 Project

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """ Initialice Food with inheritance of Snake. """

        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """ Change the position of the food. """

        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
