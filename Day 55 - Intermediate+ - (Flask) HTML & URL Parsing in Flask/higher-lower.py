# Code for Day 55 Project

from flask import Flask
from random import randint

app = Flask(__name__)
the_number = randint(0, 9)

def h1(function):
    def wrapper():
        return '<h1>' + function() + '</h1>'
    return wrapper

def add_gif(function):
    def wrapper():
        return function() + '<br><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="250">'
    return wrapper

@app.route('/')
@h1
@add_gif
def home():
    return 'Guess the number between 0 and 9'

@app.route('/<int:number>')
def check_number(number):
    if number > the_number:
        return '<h1 style="color: red">Too high</h1>' \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="250">'

    elif number < the_number:
        return '<h1 style="color: blue">Too low</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="250">'

    else:
        return '<h1 style="color: green">You found me!</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="250">'

app.run(debug=True)
