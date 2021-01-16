# Code for Day 27 practice
# Exists pack (no accuracy), place (too much accuracy, works with coords), grid (ideal one, works with rows and columns).

import tkinter

# Window for app
window = tkinter.Tk()

window.title('My first Tkinter Program')
window.minsize(width=500, height=300)

# Label for text
first_label = tkinter.Label(text='I am the label', font=('Arial', 24, 'normal'))
first_label.grid(column=0, row=0)

first_label['text'] = 'New text bro'
first_label.config(text='New text')

# Entry of text
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# Button that do something
def button_clicked():
    first_label.config(text=input.get())

button = tkinter.Button(text='Button', command=button_clicked)
button.grid(column=1, row=1)

button = tkinter.Button(text='New Button', command=button_clicked)
button.grid(column=2, row=0)

window.mainloop()
