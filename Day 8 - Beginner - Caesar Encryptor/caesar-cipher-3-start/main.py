# Code for Day 8, Exercise 6

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):

    new_text = ''

    for letter in text:

        if direction == 'encode':
            new_index = alphabet.index(letter) + shift

        elif direction == 'decode':
            new_index = alphabet.index(letter) - shift

        new_text += alphabet[new_index]

    if direction == 'encode':
        print(f'The encoded text is {new_text}')

    elif direction == 'decode':
        print(f'The decoded text is {new_text}')

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)
