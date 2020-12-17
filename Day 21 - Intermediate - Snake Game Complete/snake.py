# Class for code of Day 20 Project

from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """ Initialice the Snake. """

        self.segments = []
        for position in POSITIONS:
            self.add_segment(position)

        self.head = self.segments[0]

    def add_segment(self, position):
        """ Create a segment. """

        turtle = Turtle(shape='square')
        turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        """ Add a new segment to the Snake. """

        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Move all segments to the next segment position. """

        for segment_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment_num - 1].xcor()
            y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(x, y)

        self.head.forward(DISTANCE)

    def up(self):
        """ Move the Snake head up. """

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Move the Snake head down. """

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Move the Snake head left. """

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Move the Snake head right. """

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
