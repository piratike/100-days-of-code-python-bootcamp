# Code for Day 25 Exercises

with open('./Day 25 - Intermediate - CSV and Pandas/weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)

import csv

with open('./Day 25 - Intermediate - CSV and Pandas/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)

import pandas

data = pandas.read_csv('./Day 25 - Intermediate - CSV and Pandas/weather_data.csv')

print(data)
print(data['temp'])

print(data.to_dict())
print(data['temp'].to_list())

print(data['temp'].mean())
print(data['temp'].max())

print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

print(data[data.day == 'Monday'].temp * 9/5 + 32)

data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('./Day 25 - Intermediate - CSV and Pandas/new.csv')
