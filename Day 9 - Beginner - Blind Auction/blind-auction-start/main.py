# Code for Day 9 Project

from replit import clear
from art import logo

more = 'yes'
bidders = list()

while more == 'yes':

    print(logo)
    print('Welcome to the secret auction program!')

    bidder = dict()

    name = input('What\'s your name?: ')
    bid = input('What\'s your bid?: $')

    bidder['name'] = name
    bidder['bid'] = bid
    bidders.append(bidder)

    more = input('Are there any other bidders? Type \'yes\' or \'no\': ')

    if more == 'yes':
        clear()

    else:

        winner_bid = 0
        winner_name = ''

        for bidder in bidders:
            if int(bidder['bid']) > winner_bid:
                winner_bid = int(bidder['bid'])
                winner_name = bidder['name']

        clear()
        print('The winner is {} with a bid of ${}'.format(winner_name, winner_bid))
