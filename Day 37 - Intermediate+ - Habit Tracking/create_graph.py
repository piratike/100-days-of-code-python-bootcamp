# Code for Day 37 Project

import requests

TOKEN = 'asouihj38dh98ash78qhs910h8s7g27d09o'
USERNAME = 'piratike'

pixela_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'

print(pixela_endpoint)

graph_config = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'hours',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=pixela_endpoint, json=graph_config, headers=headers)
print(response.text)
