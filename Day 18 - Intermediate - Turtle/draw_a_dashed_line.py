# Code for Day 18 Exercise 2

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for _ in range(20):

    turtle.forward(5)
    turtle.pendown()
    turtle.forward(5)
    turtle.penup()

screen.exitonclick()
