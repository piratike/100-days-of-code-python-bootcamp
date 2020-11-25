# Code for Day 3, Exercise 4

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

final_price = 0

if size == 'S':
    final_price += 15

    if add_pepperoni == 'Y':
        final_price += 2

elif size == 'M':
    final_price += 20

    if add_pepperoni == 'Y':
        final_price += 3

elif size == 'L':
    final_price += 25

    if add_pepperoni == 'Y':
        final_price += 3

if extra_cheese == 'Y':
    final_price += 1

print('Your final bill is: ${}.'.format(final_price))
