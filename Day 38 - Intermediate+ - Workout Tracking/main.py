# Code for Day 38 Project

import requests, datetime

APP_ID = '925e6410'
API_KEY = 'e2ee0050d5d11bdb286f00db57a5d8d1'
BEARER_TOKEN = 'si74rmcsfhnov82dynovc7sy4fc893oy487fny7'
SHEETY_POST_ENDPOINT = 'https://api.sheety.co/760117026c88bf95a4871f82d651707f/workoutTracking/workouts'

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query = input('What workout did you do?: ')

parameters = {
    'query': query,
    'gender': 'male',
    'weight_kg': 80.0,
    'height_cm': 174.5,
    'age': 25
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)

workout = {
    'workout': {
        'date': datetime.datetime.now().strftime('%d/%m/%Y'),
        'time': datetime.datetime.now().strftime('%H:%M:%S'),
        'exercise': nutritionix_response.json()['exercises'][0]['user_input'].title(),
        'duration': nutritionix_response.json()['exercises'][0]['duration_min'],
        'calories': nutritionix_response.json()['exercises'][0]['nf_calories']
    }
}

headers = {
    'Authorization': 'Bearer ' + BEARER_TOKEN,
}

response = requests.post(url=SHEETY_POST_ENDPOINT, json=workout, headers=headers)
