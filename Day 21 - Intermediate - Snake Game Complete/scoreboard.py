# Class for code of Day 20 Project

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        """ Initialice Scoreboard with inheritance of Snake. """

        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(240, 270)
        self.update_score()
        self.hideturtle()

    def increase_score(self):
        """ Increase in 1 the actual score. """

        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        """ Prints the actual score. """

        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ Prints Game Over. """

        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
