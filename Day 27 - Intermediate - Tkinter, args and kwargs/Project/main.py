# Code for Day 27 Project

import tkinter

window = tkinter.Tk()

window.title('Mile to Km converter')
window.minsize(width=300, height=150)

# Entry for miles
miles_entry = tkinter.Entry(width=10)
miles_entry.grid(row=0, column=1)

# Label for miles
miles_label = tkinter.Label(text='Miles')
miles_label.grid(row=0, column=2)

# Label for equal
equal_label = tkinter.Label(text='is equal to')
equal_label.grid(row=1, column=0)

# Button for convert
def convert():
    miles = miles_entry.get()

    if miles.isdecimal():
        miles = float(miles) * 1.61
        km_result.config(text=f'{miles}')

button = tkinter.Button(text='Convert', command=convert)
button.grid(row=2, column=1)

# Label for kilometers number
km_result = tkinter.Label(text='0')
km_result.grid(row=1, column=1)

# Label for kilometers
km_label = tkinter.Label(text='Km')
km_label.grid(row=1, column=2)

window.mainloop()
