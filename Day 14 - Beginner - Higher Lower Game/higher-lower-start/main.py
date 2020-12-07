# Code for Day 14 Project

# Import art, game data and libraries needed
import random
from replit import clear
from art import logo, vs
from game_data import data

def check_response(choice, a, b):
    """ Returns True if the choice is correct, False if not. """

    if a > b and choice.lower() == 'a':
        return True

    elif a < b and choice.lower() == 'b':
        return True

    else:
        return False

# Game function
def higher_lower():
    """ Function with the Higher Lower Game. """

    clear()
    print(logo)

    score = 0
    game_end = False

    # Get First term to compare (A)
    term1 = random.choice(data)

    while not game_end:

        print('Compare A: {}, a {}, from {}.'.format(term1['name'], term1['description'], term1['country']))

        print(vs)

        # Get Second term to compare (B)
        term2 = random.choice(data)
        print('Against B: {}, a {}, from {}.'.format(term2['name'], term2['description'], term2['country']))

        # Check the response
        if check_response(input('Who has more followers? Type\'A\' or \'B\': '), term1['follower_count'], term2['follower_count']):

            clear()
            print(logo)
            score += 1
            print(f'You are right! Current score {score}.')
            term1 = term2

        else:
            clear()
            print(logo)
            print(f'Sorry, that\'s wrong. Final score: {score}')
            game_end = True

# Main Loop
while input('Do you want to play? Type \'y\' or \'n\': ') == 'y':

    higher_lower()
