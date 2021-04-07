# Class for Day 39 Capstone Project

import requests
from flight_data import FlightData

class FlightSearch:

    def __init__(self, endpoint_get, endpoint_search, token):
        
        self.endpoint_get = endpoint_get
        self.endpoint_search = endpoint_search
        self.token = token

    def get_iata_code(self, city):

        headers = {
            'apikey': self.token,
        }

        body = {
            'term': city,
            'location_types': 'city'
        }

        response = requests.get(url=self.endpoint_get, params=body, headers=headers)
        iata_code = response.json()['locations'][0]['code']

        return iata_code

    def get_flights(self, from_place, to_place, from_date, to_date):

        headers = {
            'apikey': self.token,
        }

        body = {
            'fly_from': from_place,
            'fly_to': to_place,
            'date_from': from_date,
            'date_to': to_date,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'EUR'
        }

        response = requests.get(url=self.endpoint_search, params=body, headers=headers)

        try:

            data = response.json()['data'][0]

        except IndexError:

            body['max_stopovers'] = 1

            response = requests.get(url=self.endpoint_search, params=body, headers=headers)

            try:

                data = response.json()['data'][0]

                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data['route'][0]['cityTo']
                )

                return flight_data

            except IndexError:

                return None

        else:

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
