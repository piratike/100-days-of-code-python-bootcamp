# Code for Day 18 Exercise 1

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

screen.exitonclick()
