# Code for Day 35 Project

import requests
from twilio.rest import Client

API_KEY = '37aac9be76aa301df3ae1941c28fbd88'
MY_LAT = 28.313977
MY_LNG = -16.409969
ACCOUNT_SID = 'ACcb897e2cfa6beab487ddf86b3876afbb'
AUTH_TOKEN = 'fcd693e8515a7578c3cb3c2bc4a62d18'

parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': API_KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()['hourly'][:12]

will_rain = False

for hour_data in data:

    condition_code = hour_data['weather'][0]['id']

    if int(condition_code) < 700:
        will_rain = True

if not will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
            body="It\'s going to rain, remember to take an umbrella!",
            from_='+14695157069',
            to='+34615648417'
        )
    print(message.status)
