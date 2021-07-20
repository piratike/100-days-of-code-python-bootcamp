# Code for Day 55 exercise

def logging_decorator(function):
    def wrapper(*args):
        print(f'Function called: {function.__name__}')
        print(f'The arguments are: {args[0]}, {args[1]} and {args[2]}')
        response = function(args[0], args[1], args[2])
        print(f'The function returned: {response}')
    return wrapper

@logging_decorator
def add_numbers(a, b, c):
    return a + b + c

add_numbers(3, 5, 1)
