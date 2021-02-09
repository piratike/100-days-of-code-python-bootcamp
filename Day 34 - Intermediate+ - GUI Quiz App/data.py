# Code for Day 34 Project

import requests

response_from_api = requests.get('https://opentdb.com/api.php', params={'amount': '10', 'type': 'boolean'})
response_from_api.raise_for_status()
question_data = response_from_api.json()['results']
