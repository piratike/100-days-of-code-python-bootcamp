# Code for Day 36 Project

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = 'TTSCEVM5WA14IY0K'
NEWS_API_KEY = '95ed093c13e94b9ea1d82aca9f97f94d'

ACCOUNT_SID = 'ACcb897e2cfa6beab487ddf86b3876afbb'
AUTH_TOKEN = 'fcd693e8515a7578c3cb3c2bc4a62d18'

stock_parameters = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey': STOCK_API_KEY
}

news_parameters = {
    'q' : COMPANY_NAME,
    'apikey': NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = [list(value.values()) for (key, value) in response.json()['Time Series (Daily)'].items()][:2]

yesterday_closing_price = float(data[0][-2])
before_yesterday_closing_price = float(data[1][-2])

difference_between_days = abs(before_yesterday_closing_price - yesterday_closing_price)
difference_value = before_yesterday_closing_price - yesterday_closing_price
change = (difference_between_days / yesterday_closing_price) * 100

if change > 5:

    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    data = response.json()['articles'][:3]
    articles = [[article['title'], article['description']] for article in data]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in articles:

        symbol = '🔺'

        if difference_value < 0:
            symbol = '🔻'

        body = f'{COMPANY_NAME}: {symbol}{round(change, 1)}%\n{article[0]}\n{article[1]}'

        message = client.messages.create(
                body=body,
                from_='+14695157069',
                to='+34615648417'
            )
