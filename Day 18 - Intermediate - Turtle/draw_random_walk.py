# Code for Day 18 Exercise 3

import random
from turtle import Turtle, colormode,Screen


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle = Turtle()
screen = Screen()
colormode(255)
choices = ['forward', 'left', 'right', 'back']
turtle.speed('normal')
turtle.width(10)

for _ in range(200):

    choice = random.choice(choices)
    turtle.color(random_color())

    if choice == 'forward':
        turtle.forward(25)

    elif choice == 'left':
        turtle.left(90)
        turtle.forward(25)

    elif choice == 'right':
        turtle.right(90)
        turtle.forward(25)

    elif choice == 'back':
        turtle.backward(25)

screen.exitonclick()
