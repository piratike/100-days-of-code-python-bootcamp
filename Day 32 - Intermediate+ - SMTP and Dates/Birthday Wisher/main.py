# Code for Day 32 Project

import pandas, datetime, random, smtplib

data = pandas.read_csv('./Day 32 - Intermediate+ - SMTP and Dates/Birthday Wisher/birthdays.csv')
birthdays = {(value['month'], value['day']): value for (index, value) in data.iterrows()}

today = datetime.datetime.now()
today = (today.month, today.day)

if today in birthdays:

    letter_num = random.randint(1, 3)

    with open(f'./Day 32 - Intermediate+ - SMTP and Dates/Birthday Wisher/letter_templates/letter_{letter_num}.txt', 'r') as file:
        letter = file.read()

    letter = letter.replace('[NAME]', birthdays[today]['name'])
    my_email = 'email@gmail.com'
    my_password = 'password'

    with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='kevin.mrosa96@gmail.com',
                msg=f'Subject:Happy Birthday\n\n{letter}'
            )
