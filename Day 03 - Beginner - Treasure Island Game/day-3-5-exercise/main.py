# Code for Day 3, Exercise 5

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = list()
love = list()

for letter in 'true':
    true.append(name1.lower().count(letter) + name2.lower().count(letter))

for letter in 'love':
    love.append(name1.lower().count(letter) + name2.lower().count(letter))

score = int(str(sum(true)) + str(sum(love)))

if score > 90 or score < 10:
    print('Your score is {}, you go together like coke and mentos.'.format(score))

elif score > 40 and score < 50:
    print('Your score is {}, you are alright together.'.format(score))

else:
    print('Your score is {}.'.format(score))
