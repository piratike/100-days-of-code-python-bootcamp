# Code for Day 37 Project

import requests, datetime

TOKEN = 'asouihj38dh98ash78qhs910h8s7g27d09o'
USERNAME = 'piratike'
GRAPH_ID = 'graph1'
DATE = datetime.datetime(year=2021, month=3, day=23).strftime('%Y%m%d')

pixela_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}'

parameters = {
    'quantity': '4',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.put(url=pixela_endpoint, json=parameters, headers=headers)
print(response.text)