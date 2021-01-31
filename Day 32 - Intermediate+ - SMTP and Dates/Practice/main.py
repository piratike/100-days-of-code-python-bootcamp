# Code for Day 32 practice

import smtplib, datetime, random

my_email = 'email@gmail.com'
my_password = 'password'

with open('./Day 32 - Intermediate+ - SMTP and Dates/Practice/quotes.txt', 'r') as file:
    quotes = file.readlines()

today = datetime.datetime.now()

if today.weekday() == 0:    # 0 Monday - 6 Sunday

    quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='kevin.mrosa96@gmail.com',
            msg=f'Subject:Good morning!\n\n{quote}'
        )
