# Code for Day 15 Project

# Importing data needed
from data import menu, resources, coins


# TODO: 1. Prompt user by asking "What would you like?" (espresso/latte/cappuccino).
def ask():
    user_response = input('What would you like? (espresso/latte/cappuccino): ')
    return user_response


# TODO: 3. Print report.
def print_report():
    for resource in resources:
        print(f'{resource}: {resources[resource]}')

    print(f'Money: ${machine_money}')


# TODO: 4. Check resources sufficient.
def check_resources(drink):
    for resource in menu[drink]['ingredients']:
        if resources[resource] < menu[drink]['ingredients'][resource]:
            print(f'Sorry, not enough {resource}')
            return False

    return True


# TODO: 5. Process coins.
def ask_for_coins():
    print('Please insert coins.')
    money = dict()

    for coin in coins:
        money[coin] = int(input(f'How many {coin}?: '))

    return money


# TODO: 6. Check transaction succesful.
def check_payment(coins_given, drink_selected):
    payed = 0

    for coin in coins_given:
        payed += coins[coin] * coins_given[coin]

    if menu[drink_selected]['cost'] <= payed:
        return payed - menu[drink_selected]['cost']

    return False


# TODO: 7. Make Coffee.
def make_coffee(choice_given, change_calculated):
    print(f'Here is ${round(change_calculated, 2)} in change.')
    print(f'Here is your {choice_given}, enjoy!')

    for resource in menu[choice_given]['ingredients']:
        resources[resource] -= menu[choice_given]['ingredients'][resource]

    return menu[choice_given]['cost']


# Main Loop
machine_money = 0
machine_on = True

while machine_on:

    choice = ask()

    # TODO: 2. Turn off the Coffee Machine bu entering "off" to the prompt.
    if choice == 'off':
        machine_on = False

    elif choice == 'report':
        print_report()

    elif choice in menu:

        if check_resources(choice):
            coins_inserted = ask_for_coins()
            change = check_payment(coins_inserted, choice)

            if change is not bool:
                machine_money += make_coffee(choice, change)

            else:
                print('Sorry, not enough money inserted.')

    else:
        print('Choice not allowed, try other thing.')
