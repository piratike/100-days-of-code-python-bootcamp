# Code for Day 31 Capstone Project, Flash Card App

BACKGROUND_COLOR = "#B1DDC6"

import tkinter, pandas, random

# Get Data from csv
try:

    words = pandas.read_csv('./Day 31 - Intermediate - Flash Card/data/words_to_learn.csv')
    words = words.to_dict(orient='records')

except FileNotFoundError:

    words = pandas.read_csv('./Day 31 - Intermediate - Flash Card/data/french_words.csv')
    words = words.to_dict(orient='records')

current_card = {}

# Function to flip the card
def flip_card():

    canvas.itemconfig(lenguage_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=second_image)

# Function to save the progress of the user
def is_known():

    words.remove(current_card)
    dataframe = pandas.DataFrame(words)
    dataframe.to_csv('./Day 31 - Intermediate - Flash Card/data/words_to_learn.csv')
    pick_new_word()

# Function to pick a new random word
def pick_new_word():

    global current_card
    canvas.itemconfig(card_bg, image=first_image)
    canvas.itemconfig(lenguage_text, text='French', fill='black')
    current_card = random.choice(words)
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    window.after(3000, flip_card)

# Initialice App window
window = tkinter.Tk()
window.title('Flash Cards')
window.minsize(width=500, height=400)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Buttons for the App
right_image = tkinter.PhotoImage(file='./Day 31 - Intermediate - Flash Card/images/right.png')
wrong_image = tkinter.PhotoImage(file='./Day 31 - Intermediate - Flash Card/images/wrong.png')

right_button = tkinter.Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=pick_new_word)

right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

# Card canvas
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
first_image = tkinter.PhotoImage(file='./Day 31 - Intermediate - Flash Card/images/card_front.png')
second_image = tkinter.PhotoImage(file='./Day 31 - Intermediate - Flash Card/images/card_back.png')
card_bg = canvas.create_image(400, 260, image=first_image)
lenguage_text = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

pick_new_word()

window.mainloop()
