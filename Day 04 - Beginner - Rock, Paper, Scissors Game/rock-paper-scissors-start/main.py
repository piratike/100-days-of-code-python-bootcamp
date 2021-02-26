# Code for Day 4 project

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: ')

choices = list((rock, paper, scissors))
pc_choice = choices[random.randint(0, 2)]

print(pc_choice, choices[int(human_choice)])

if (human_choice == '0' and pc_choice == rock) or (human_choice == '1' and pc_choice == paper) or (human_choice == '2' and pc_choice == scissors):
    print('It\'s a draw.')

if (human_choice == '0' and pc_choice == scissors) or (human_choice == '1' and pc_choice == rock) or (human_choice == '2' and pc_choice == paper):
    print('You Win!')

if (human_choice == '0' and pc_choice == paper) or (human_choice == '1' and pc_choice == scissors) or (human_choice == '2' and pc_choice == rock):
    print('You Lose...')
