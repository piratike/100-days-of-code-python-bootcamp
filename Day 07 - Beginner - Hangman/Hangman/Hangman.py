# Code for Hangman Game - Kevin Machuca

import random
from hangman_words import word_list # Import the entire word list
from hangman_art import stages      # Import the stages ascii art
from hangman_art import logo        # Import the game logo ascii art

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
display = list()

for i in range(len(chosen_word)):
    display.append('_')

print(f"{' '.join(display)}")
print(stages[lives])

while not end_of_game:

  guess = input("Guess a letter: ").lower()

  # Reveal the correct letters
  for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess

  # Check if user is wrong.
  if guess not in chosen_word:

      print('You guess {}, that\'s not in the word. You lose 1 life.'.format(guess))

      lives -= 1

      if lives == 0:
          end_of_game = True
          print("You lose.")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(stages[lives])
