from turtle import Turtle, Screen
import random

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = Screen()

screen.setup(500, 400)

turtles = []
pos = 150
bet = screen.textinput(title='Make your bet', prompt='Wich turtle will win the race? Enter a color (Red, Orange, '
                                                     'Yellow, Green , Blue, Purple): ').lower()

for colour in colours:
    turtle = Turtle(shape='turtle')
    turtle.color(colour)
    turtle.penup()
    turtle.goto(-230, pos)
    pos -= 50
    turtles.append(turtle)

game = True
winner = ''

while game:

    for turtle in turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.pos()[0] > 230:
            winner = turtle.color()[0]
            game = False

if winner == bet:
    print(f'Great! {winner} win!')

else:
    print(f'You lose, {winner} wins.')

screen.exitonclick()
