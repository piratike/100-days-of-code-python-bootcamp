# Code for Day 26 Project

import pandas

alphabet = pandas.read_csv('./Day 26 - Intermediate - List Comprehension/Project/nato_phonetic_alphabet.csv')
alphabet = {row.letter:row.code for (index, row) in alphabet.iterrows()}

word = input('Enter a word: ')
code_words = [alphabet[letter.upper()] for letter in word]

print(code_words)
