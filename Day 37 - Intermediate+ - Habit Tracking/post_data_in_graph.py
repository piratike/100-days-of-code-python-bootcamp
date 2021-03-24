# Code for Day 37 Project

import requests, datetime

TOKEN = 'asouihj38dh98ash78qhs910h8s7g27d09o'
USERNAME = 'piratike'
GRAPH_ID = 'graph1'

pixela_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}'

parameters = {
    'date': datetime.datetime.now().strftime('%Y%m%d'),
    'quantity': '2',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=pixela_endpoint, json=parameters, headers=headers)
print(response.text)