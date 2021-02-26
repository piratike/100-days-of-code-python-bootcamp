# Code for Caesar Encyptor / Decryptor - Kevin Machuca

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

def caesar(text, shift, direction):

    new_text = ''

    for letter in text:

        if not letter in alphabet:
            new_text += letter
            continue

        if shift >= len(alphabet):
            shift = shift % len(alphabet)

        if direction == 'encode':
            new_index = alphabet.index(letter) + shift

        elif direction == 'decode':
            new_index = alphabet.index(letter) - shift

        if new_index >= len(alphabet):
                new_index = len(alphabet) - new_index

        new_text += alphabet[new_index]

    if direction == 'encode':
        print(f'The encoded text is {new_text}')

    elif direction == 'decode':
        print(f'The decoded text is {new_text}')

print(logo)

exit = False

while(not exit):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    choice = input('Type \'yes\' if you want to go again. Otherwise type \'no\': ')

    if choice == 'no':
        exit = True
