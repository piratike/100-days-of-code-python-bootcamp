# Code for Day 30, Exercise 1

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):

    try:

        fruit = fruits[index]

    except IndexError:

        print("Fruit pie")

    else:
        print(fruit + " pie")

make_pie(4)
