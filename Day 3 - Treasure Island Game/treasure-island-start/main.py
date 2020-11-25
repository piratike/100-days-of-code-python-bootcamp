# Code for Day 3 Project

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print('You are in the beach. On the right, you see a cavern. On the left, you see a pier.')

first_choice = input('Where are you going? ("L" or "R"): ')

if first_choice == 'R':
    print('You fall into a hole. Game Over.')

else:
    print('You reach the pier. You can wait there or start swimming to reach a distant island.')

    second_choice = input('What do you do? ("W" or "S"): ')

    if second_choice == 'S':
        print('A trout attack you. Game Over.')

    else:

        print('While you wait a big boat with three doors arrives the pier. The doors are Red, Blue and Yellow.')

        third_choice = input('Which door do you choose? ("R", "B" or "Y"): ')

        if third_choice == 'R':
            print('You get burned by fire. Game Over.')

        elif third_choice == 'B':
            print('You get eaten by beasts. Game Over.')

        elif third_choice == 'Y':
            print('You win!')

        else:
            print('Game Over.')
