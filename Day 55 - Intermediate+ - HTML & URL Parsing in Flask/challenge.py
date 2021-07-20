# Code for Day 55 challenge

from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper

def emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper

def underline(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper

@app.route('/')
@bold
@emphasis
@underline
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
