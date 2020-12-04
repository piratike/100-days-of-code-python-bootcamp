"""
    12/2020, Kevin Machuca
"""
# Code for Day 12 Project

import random
from art import logo

# Functions declaration

def get_lives(difficulty):
    """ Return the number of lives to play. """

    if difficulty == 'easy':
        return 10

    elif difficulty == 'hard':
        return 5

    else:
        return 0

def compare_guess(number_to_guess, number_input):
    """ Check the number given  """

    if number_input < number_to_guess:
        return False, 'Too low.\nGuess again.'

    elif number_input > number_to_guess:
        return False, 'Too high.\nGuess again.'

    elif number_input == number_to_guess:
        return True, f'You got it! The answer was {number_to_guess}.'

    else:
        return False, 'Bad input, try again.'

def number_guessing():
    """ Start the game fo The Number Guessing """

    print(logo)

    print('Welcome to The Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

    lives = get_lives(difficulty)
    number_to_guess = random.choice(range(101))
    game_end = False

    while not game_end:

        if lives > 0:

            print(f'You have {lives} attemps remaining.')
            guess = int(input('Make a guess: '))

            game_end, message = compare_guess(number_to_guess, guess)
            lives -= 1
            print(message)

        else:
            game_end = True
            print('You have run out of attemps, you lose...')

# Main Code

while input('Do you want to play? Type \'y\' or \'n\': ') == 'y':
    number_guessing()
