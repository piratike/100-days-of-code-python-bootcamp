# Code for Day 40 Capstone Project

# Class for Day 39 Capstone Project

import requests

class UsersManager:

    def __init__(self, endpoint, token):

        self.endpoint = endpoint
        self.token = token

    def get_users(self):

        headers = {
            'Authorization': 'Bearer ' + self.token,
        }

        response = requests.get(url=self.endpoint, headers=headers)
        sheet_data = response.json()['users']

        return sheet_data

    def signup_user(self):

        print('##### Welcome to the Flight Club #####\n')
        print('I find the best flight prices and email you :D\n')

        name = input('-> What\'s your first name?: ')
        last_name = input('-> What\'s your last name?: ')

        email_confirmed = False

        while not email_confirmed:

            email = input('-> What\'s your email?: ')
            email_confirmation = input('-> Type tour email again: ')

            if email == email_confirmation:
                email_confirmed = True
                print('\nGreat, you are in the club now!')

            else:
                print('\nPlease enter the correct email :(')

        headers = {
            'Authorization': 'Bearer ' + self.token,
        }        

        body = {
            'user': {
                'firstName': name,
                'lastName': last_name,
                'email': email
            }
        }

        requests.post(url=self.endpoint, json=body, headers=headers)
