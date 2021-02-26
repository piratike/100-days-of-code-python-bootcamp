# Code for Day 4, Exercise 2

import random

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

print('{} is going to buy the meal today!'.format(names[random.randint(0, len(names) - 1)]))
