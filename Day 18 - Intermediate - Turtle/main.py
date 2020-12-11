# Code for Day 18 Project

import colorgram, random
from turtle import Turtle, colormode, Screen

turtle = Turtle()
screen = Screen()

colormode(255)
turtle.speed('fastest')

colors_list = colorgram.extract('Me.jpg', 10)
colors_tuples = list()

for color in colors_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_tuples.append(new_color)

turtle.penup()
turtle.goto(-200, -200)

for i in range(10):

    for j in range(10):
        turtle.pendown()
        turtle.color(random.choice(colors_tuples))
        turtle.dot(20)
        turtle.penup()
        turtle.goto(turtle.xcor() + 50, turtle.ycor())

    turtle.goto(-200, turtle.ycor() + 50)

screen.exitonclick()
