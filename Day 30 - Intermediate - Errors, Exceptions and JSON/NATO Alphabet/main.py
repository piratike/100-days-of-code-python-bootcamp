# Code for Day 26 Project

import pandas

alphabet = pandas.read_csv('./Day 30 - Intermediate - Errors, Exceptions and JSON/NATO Alphabet/nato_phonetic_alphabet.csv')
alphabet = {row.letter:row.code for (index, row) in alphabet.iterrows()}

word = input('Enter a word: ')

try:

    code_words = [alphabet[letter.upper()] for letter in word]
    print(code_words)

except KeyError:

    print('Sorry, only letters can be entered!!')
