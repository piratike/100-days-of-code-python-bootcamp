# Code for Day 39 Capstone Project

import datetime
from flight_search import FlightSearch
from data_manager import DataManager

SHEETY_GET_ENDPOINT = 'https://api.sheety.co/760117026c88bf95a4871f82d651707f/flightDeals/prices'
SHEETY_BEARER_TOKEN = 'si74rmcsfhnov82dynovc7sy4fc893oy487fny7'
KIWI_GET_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'
KIWI_SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
KIWI_BEARER_TOKEN = 'kd3SUVwKmkWaXMM1F9-GJzxp8sjOAKvv'

DM = DataManager(endpoint=SHEETY_GET_ENDPOINT, token=SHEETY_BEARER_TOKEN)
FS = FlightSearch(endpoint_get=KIWI_GET_ENDPOINT, endpoint_search=KIWI_SEARCH_ENDPOINT, token=KIWI_BEARER_TOKEN)

data_from_sheet = DM.get_data()
flights_data = []

for data in data_from_sheet:

    if not data['iataCode']:
        data['iataCode'] = FS.get_iata_code(data['city'])
        DM.put_data(data)

    flight_data = FS.get_flights('MAD', data['iataCode'], (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y'), (datetime.datetime.now() + datetime.timedelta(days=60)).strftime('%d/%m/%Y'))
    flights_data.append({
        'price': flights_data['price'],
        'origin_city': flights_data['origin_city'],
        'origin_airport': flights_data['origin_airport'],
        'destination_city': flights_data['destination_city'],
        'destination_airport': flights_data['destination_airport'],
        'out_date': flights_data['out_date'],
        'return_date': flights_data['return_date']
    })

print(flights_data)
