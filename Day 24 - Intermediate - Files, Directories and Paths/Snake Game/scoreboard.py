# Class for code of Day 20 Project

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        """ Initialice Scoreboard with inheritance of Snake. """

        super().__init__()
        self.score = 0

        with open('Day 24 - Intermediate - Files, Directories and Paths/Snake Game/data.txt', 'r') as score:
            self.highscore = int(score.read())

        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def increase_score(self):
        """ Increase in 1 the actual score. """

        self.score += 1
        self.update_score()

    def update_score(self):
        """ Prints the actual score. """

        self.clear()
        self.write(f'Score: {self.score} High Socre: {self.highscore}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ Prints Game Over. """

        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def reset(self):
        """ Reset the Scoreboard and saves the score if it is the higher score. """

        if self.highscore < self.score:
            self.highscore = self.score
            with open('Day 24 - Intermediate - Files, Directories and Paths/data.txt', 'w') as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_score()
