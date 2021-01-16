# Code for Day 27 practice

import tkinter

# Window for app
window = tkinter.Tk()

window.title('My first Tkinter Program')
window.minsize(width=500, height=300)

# Label for text
first_label = tkinter.Label(text='I am the label', font=('Arial', 24, 'normal'))
first_label.pack()

first_label['text'] = 'New text bro'
first_label.config(text='New text')

# Entry of text
input = tkinter.Entry(width=10)
input.pack()

# Button that do something
def button_clicked():
    first_label.config(text=input.get())

button = tkinter.Button(text='Change', command=button_clicked)
button.pack()

# Multyline text
text = tkinter.Text()
text.focus()
text.insert(tkinter.END, 'Example of multi-line text entry.')
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=10, width=5, command=scale_used)
scale.pack()

# Check button
def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text='Is on?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radio button
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Window stay open
window.mainloop()
