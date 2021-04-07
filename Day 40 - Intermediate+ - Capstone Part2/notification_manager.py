# Class for Day 39 Capstone Project

import smtplib
from twilio.rest import Client

class NotificationManager:

    def __init__(self, sid, token):

        self.account_sid = sid
        self.auth_token = token
    
    def send_sms(self, flight, stop_over=False):

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

        if stop_over:
            body = body + '\nFlight has 1 stop over, via {}'.format(stop_over)

        message = client.messages.create(
                body=body,
                from_='+14695157069',
                to='+34615648417'
            )

    def send_emails(self, flight, users):

        my_email = 'tutotronik@gmail.com'
        my_password = 'Kevin12011996'

        for user in users:

            message = 'Subject:Cheap flight\n\nLow price alert! Only {}€ to fly from {}-{} to {}-{}, from {} to {}.'.format(
                        flight.price,
                        flight.origin_city,
                        flight.origin_airport,
                        flight.destination_city,
                        flight.destination_airport,
                        flight.out_date,
                        flight.return_date
                    )

            message = message + '\nhttps://www.google.es/travel/flights?hl=es#flt={}.{}.{}*{}.{}.{}'.format(
                flight.origin_airport,
                flight.destination_airport,
                flight.out_date,
                flight.destination_airport,
                flight.origin_airport,
                flight.return_date
            )

            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=user['email'],
                    msg=message.encode('utf-8')
                )
