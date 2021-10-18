# Text to Morse Code Converter - converter.py
# kevin.mrosa96@gmail.com - 10/2021

from replit import clear

class Converter:

    def __init__(self, logo, letters_in_morse):
        self.logo = logo
        self.letters_in_morse = letters_in_morse

    """ Print in console the input given converted into morse code. """
    def print_converted(self, input):
        print(f'{input.capitalize()} in Morse Code is:')
        morse = []

        for char in input:
            morse.append(self.letters_in_morse[char])

        print(' '.join(morse))

    """ Check in the given input for digits. """
    def has_numbers(self, input):
        return any(char.isdigit() for char in input)

    """ Execute a loop to ask the user for texts to convert to morse. """
    def run_prog(self):

        while True:

            print(self.logo)
            text_to_convert = input('\n=> Give a text to convert to Morse Code (No numbers except 0 to exit):').lower()

            if not self.has_numbers(text_to_convert):
                clear()
                self.print_converted(text_to_convert)

            else:
                if text_to_convert == '0':
                    break

                else:
                    clear()
                    print('<<<<<< The Morse Converter only accept letters, not numbers! >>>>>>\n\n')
