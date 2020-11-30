# Code for Day 8, Exercise 1

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():

    print('Hello World!')
    print('Nice to meet you.')
    print('Bye, I\'ll see you other day.')

greet()

def greet_with_name(name):

    print(f'Hello {name}!')
    print(f'Nice to meet you {name}.')

greet_with_name('Kevin')

def greet_with(name, location):

    print(f'Hello {name}!')
    print(f'What is it like in {location}?')

greet_with(name='Jhon', location='The Wall')
