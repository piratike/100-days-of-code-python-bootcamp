# Code for Day 47 Project

import requests, smtplib
from bs4 import BeautifulSoup

ITEM_URL = 'https://www.amazon.es/MSI-Infinite-Plus-9SD-492XIB-Ordenador/dp/B07Z8LCLLF/ref=lp_11606846031_1_9?s=specialty-aps'
MY_EMAIL = 'email@gmail.com'
MY_PASSWORD = 'password'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
}

item_webpage = requests.get(url=ITEM_URL, headers=headers)

try:

    soup = BeautifulSoup(item_webpage.text, 'html.parser')
    item_price = float(
        soup.find(name='span', class_='priceBlockBuyingPriceString')
        .getText()
        .split()[0]
        .replace('.', '')
        .replace(',', '.')
    )

    if item_price < (item_price - item_price * 0.3):

        letter = f'Hey, this product is under the target price! Buy it now... {ITEM_URL}'

        with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs='kevin.mrosa96@gmail.com',
                    msg=f'Subject:Amazon tracker\n\n{letter}'
                )

except:

    pass
