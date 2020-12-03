# Code for Day 11 Project

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo


def deal_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])


def calculate_score(cards):

    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1

    return sum(cards)


def compare(user, computer):

    if computer == 0 or user > 21:
        return 'You lose...'

    elif user == 0 or computer > 21:
        return 'You win!'

    elif computer > user:
        return 'You lose...'

    elif computer < user:
        return 'You win!'

    elif user == computer:
        return 'It\'s a Draw.'

    return 'You lose'

def blackjack():

    print(logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    game_end = False

    while not game_end:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your cards {user_cards} (Score: {user_score}).')
        print(f'Computer\'s first card {computer_cards[0]}.')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True

        else:

            choice = input(
                'Do you want to get another card? Type \'y\' or \'n\': ')

            if choice == 'y':
                user_cards.append(deal_card())

            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final cards: {user_cards} (Score: {user_score}).')
    print(f'Computer\'s final cards: {computer_cards} (Score: {computer_score}).')
    print(compare(user_score, computer_score))

while input('Do you want to play? Type \'y\' or \'n\': ') == 'y':
    clear()
    blackjack()
