# Code for Day 18 Exercise 4

import random
from turtle import Turtle, colormode, Screen


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle = Turtle()
screen = Screen()
colormode(255)
turtle.speed('fastest')
num_circles = 100

for _ in range(num_circles):

    turtle.color(random_color())
    turtle.circle(200)
    turtle.right(360/num_circles)

screen.exitonclick()
