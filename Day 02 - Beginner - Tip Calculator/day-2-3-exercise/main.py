# Code for Day 2, Exercise 3

age = input("What is your current age? ")

left_years = 90 - int(age)
left_months = left_years * 12
left_weeks = left_months * 4
left_days = left_weeks * 7

print('You have {} days, {} weeks, and {} months left.'.format(left_days, left_weeks, left_months))
