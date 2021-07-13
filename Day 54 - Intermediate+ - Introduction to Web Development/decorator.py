# Code for Day 54 exercises

def delay_decorator(function):
    def do_something():
        print('Testing decorator...')
        function()
        print('It works!')

    return do_something

@delay_decorator
def func_1():
    print('Function 1!')

def func_2():
    print('Function 2...')

func_1()
func_2()
