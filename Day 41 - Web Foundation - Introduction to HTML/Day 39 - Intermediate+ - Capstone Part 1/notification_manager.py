# Class for Day 39 Capstone Project

import requests
from twilio.rest import Client

class NotificationManager:

    def __init__(self, sid, token):

        self.account_sid = sid
        self.auth_token = token
    
    def send_sms(self, flight):

        client = Client(self.account_sid, self.auth_token)

        body = 'Low price alert! Only {}€ to fly from {}-{} to {}-{}, from {} to {}.'.format(
            flight.price,
            flight.origin_city,
            flight.origin_airport,
            flight.destination_city,
            flight.destination_airport,
            flight.out_date,
            flight.return_date
        )

        message = client.messages.create(
                body=body,
                from_='+14695157069',
                to='+34615648417'
            )
