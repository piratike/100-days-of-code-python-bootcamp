# Code for Day 10 Project

from art import logo

def add(a, b):
    """ Add the two given numbers and return the result. """
    return a + b

def substract(a, b):
    """ Substract the two given numbers and return the result. """
    return a - b

def multiply(a, b):
    """ Multiply the two given numbers and return the result. """
    return a * b

def divide(a, b):
    """ Divide the two given numbers and return the result. """
    return a / b

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

print(logo)

number1 = float(input('What\'s the first number?: '))
operators = ''
for operation in operations:
    operators += operation + ' '
print(operators)
operation = input('Pick an operation from the line above: ')
number2 = float(input('What\'s the second number?: '))

result = ''
exit = False

while not exit:

    if result != '':
        choice = input('Type \'y\' to continue calculating with {}, or type \'n\' to exit: '.format(result))

        if choice == 'y':
            number1 = result
            operation = input('Pick an operation: ')
            number2 = float(input('What\'s the next number?: '))

        else:
            exit = True

    if operation in operations:
        result = operations[operation](number1, number2)
        print(f'{number1} {operation} {number2} = {result}')

    else:
        print('It\'s not a valid operation...')
