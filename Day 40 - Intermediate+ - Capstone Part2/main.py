# Code for Day 39 Capstone Project

import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from users_manager import UsersManager

SHEETY_GET_ENDPOINT = 'https://api.sheety.co/760117026c88bf95a4871f82d651707f/flightDeals/prices'
SHEETY_POST_ENDPOINT = 'https://api.sheety.co/760117026c88bf95a4871f82d651707f/flightDeals/users'
SHEETY_BEARER_TOKEN = 'si74rmcsfhnov82dynovc7sy4fc893oy487fny7'
KIWI_GET_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'
KIWI_SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
KIWI_BEARER_TOKEN = 'kd3SUVwKmkWaXMM1F9-GJzxp8sjOAKvv'
TWILIO_ACCOUNT_SID = 'ACcb897e2cfa6beab487ddf86b3876afbb'
TWILIO_AUTH_TOKEN = 'fcd693e8515a7578c3cb3c2bc4a62d18'

DM = DataManager(endpoint=SHEETY_GET_ENDPOINT, token=SHEETY_BEARER_TOKEN)
FS = FlightSearch(endpoint_get=KIWI_GET_ENDPOINT, endpoint_search=KIWI_SEARCH_ENDPOINT, token=KIWI_BEARER_TOKEN)
NM = NotificationManager(sid=TWILIO_ACCOUNT_SID, token=TWILIO_AUTH_TOKEN)
UM = UsersManager(endpoint=SHEETY_POST_ENDPOINT, token=SHEETY_BEARER_TOKEN)

data_from_sheet = DM.get_data()

for data in data_from_sheet:

    if not data['iataCode']:
        data['iataCode'] = FS.get_iata_code(data['city'])
        DM.put_data(data)

    flight = FS.get_flights('MAD', data['iataCode'], (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y'), (datetime.datetime.now() + datetime.timedelta(days=60)).strftime('%d/%m/%Y'))

    if flight and float(flight.price) < float(data['lowestPrice']):
        NM.send_sms(flight)
        users = UM.get_users()
        NM.send_emails(flight, users)
