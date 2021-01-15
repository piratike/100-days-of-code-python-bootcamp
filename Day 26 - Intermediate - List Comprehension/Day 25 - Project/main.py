# Code for Day 25 Project

import turtle, pandas

url_to_img = './Day 26 - Intermediate - List Comprehension/Day25 - Project/blank_states_img.gif'
url_to_df = './Day 26 - Intermediate - List Comprehension/Day25 - Project/50_states.csv'
url_to_learn = './Day 26 - Intermediate - List Comprehension/Day25 - Project/states_to_learn.csv'

df = pandas.read_csv(url_to_df)
states = df['state'].to_list()

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(url_to_img)

turtle.shape(url_to_img)

game_on = True
guesses = []
score = 0

while len(guesses) <= len(states):

    answer_state = screen.textinput(title=f'{score}/50 Guess the State', prompt='What\'s another state\'s name?').title()

    if answer_state == 'Exit':

        states_to_learn = [state for state in states if state not in guesses]   # already done xD
        pandas.DataFrame(states_to_learn).to_csv(url_to_learn)
        break

    if answer_state in states:

        guesses.append(answer_state)
        score += 1
        x_coor = int(df[df.state == answer_state].x)
        y_coor = int(df[df.state == answer_state].y)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coor, y_coor)
        t.write(answer_state)
