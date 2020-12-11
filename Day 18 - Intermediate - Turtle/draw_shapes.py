# Code for Day 18 Exercise 3

import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
sides = 3
turns = 0

for _ in range(9):

    turtle.color(random.choice(colours))

    while turns != sides:
        turtle.forward(100)
        turtle.right(360/sides)
        turns += 1

    turns = 0
    sides += 1

screen.exitonclick()
