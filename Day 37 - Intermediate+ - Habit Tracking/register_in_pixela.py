# Code for Day 37 Project

import requests

pixela_endpoint_for_register = 'https://pixe.la/v1/users'

user_params = {
    'token': 'asouihj38dh98ash78qhs910h8s7g27d09o',
    'username': 'piratike',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint_for_register, json=user_params)
print(response.text)
