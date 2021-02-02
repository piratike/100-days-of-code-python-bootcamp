# Code for Day 33 Project

import requests, datetime, time, smtplib

MY_LAT = 28.313977
MY_LNG = -16.409969

my_email = 'email@gmail.com'
my_password = 'password'

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset_time = int(data['results']['sunset'].split('T')[1].split(':')[0])

def is_up(latitude, longitude):

    if latitude < (MY_LAT + 5) or latitude > (MY_LAT - 5):
        if longitude < (MY_LNG + 5) or longitude > (MY_LNG - 5):
            return True

    return False

def is_dark(sunrise, sunset):

    now = datetime.datetime.now()

    if now.hour > sunset or now.hour < sunrise:
        return True

    return False

def send_email():

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='kevin.mrosa96@gmail.com',
            msg='Subject:ISS position\n\nLook up.'
        )

while True:

    if is_up(iss_latitude, iss_longitude) and is_dark(sunrise_time, sunset_time):
        send_email()

    time.sleep(60)
