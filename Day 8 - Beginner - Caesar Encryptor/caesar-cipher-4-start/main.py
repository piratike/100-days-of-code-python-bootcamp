# Code for Day 8, Exercise 7

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo    # TODO-1

def caesar(text, shift, direction): # My function

    new_text = ''

    for letter in text:

        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"

        if not letter in alphabet:
            new_text += letter
            continue

        if shift >= len(alphabet):
            shift = shift % len(alphabet)

        if direction == 'encode':
            new_index = alphabet.index(letter) + shift

        elif direction == 'decode':
            new_index = alphabet.index(letter) - shift

        new_text += alphabet[new_index]

    if direction == 'encode':
        print(f'The encoded text is {new_text}')

    elif direction == 'decode':
        print(f'The decoded text is {new_text}')

# TODO-1: Import and print the logo from art.py when the program starts.

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a new function that calls itself if they type 'yes'. 

exit = False

while(not exit):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Hint: Think about how you can use the modulus (%).

    caesar(text, shift, direction)

    choice = input('Type \'yes\' if you want to go again. Otherwise type \'no\': ')

    if choice == 'no':
        exit = True
