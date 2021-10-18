# Text to Morse Code Converter - main.py
# kevin.mrosa96@gmail.com - 10/2021

from art import logo
from letters import letters
from converter import Converter

prog = Converter(logo, letters)
prog.run_prog()
