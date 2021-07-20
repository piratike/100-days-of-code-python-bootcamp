# Code for Day 54 practice exercise

import time

def speed_calc_decorator(function):

    def wrapper():
        starting_time = time.time()
        function()
        finishing_time = time.time()
        print('Time taken:' + str(finishing_time - starting_time) + ' seconds.')

    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
