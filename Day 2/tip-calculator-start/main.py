# Code for Day 2 Project

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill = float(input('What was the total bill?: '))
tip = int(input('What percentage tip would you like to give, 10, 12 or 15?: '))
people = int(input('How many people to split the bill?: '))

each_price = round((bill + bill * (tip / 100)) / people, 2)

print('Each person should pay: ${}'.format(each_price))
