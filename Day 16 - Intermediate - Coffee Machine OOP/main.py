from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Main Loop
machine_money = 0
machine_on = True

# Classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:

    choice = input(f'What would you like? ({menu.get_items()}): ')

    if choice == 'off':
        machine_on = False

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    elif choice in menu.get_items() and choice:

        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):

            if money_machine.make_payment(menu.find_drink(choice).cost):

                coffee_maker.make_coffee(menu.find_drink(choice))

    else:
        print('Choice not allowed, try other thing.')
