# Class for Day 39 Capstone Project

import requests

class DataManager:

    def __init__(self, endpoint, token):
        
        self.endpoint = endpoint
        self.token = token

    def get_data(self):

        headers = {
            'Authorization': 'Bearer ' + self.token,
        }

        response = requests.get(url=self.endpoint, headers=headers)
        sheet_data = response.json()['prices']

        return sheet_data

    def put_data(self, row):

        headers = {
            'Authorization': 'Bearer ' + self.token,
        }        

        body = {
            'price': row
        }

        requests.put(url='{}/{}'.format(self.endpoint, row['id']), json=body, headers=headers)
