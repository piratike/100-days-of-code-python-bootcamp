# Code for Day 28 Project

import tkinter, random, pyperclip
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pwd_letters = random.sample(letters, int(nr_letters))
    pwd_numbers = random.sample(numbers, int(nr_numbers))
    pwd_symbols = random.sample(symbols, int(nr_symbols))

    pwd = pwd_letters + pwd_numbers + pwd_symbols
    random.shuffle(pwd)
    pwd = ''.join(pwd)

    pyperclip.copy(pwd)
    password_entry.insert(0, pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()

    if not website:
        tkinter.messagebox.showwarning(title='Error', message='Please don\'t leave the website field empty!')
        return False

    email = email_entry.get()

    if not email:
        tkinter.messagebox.showwarning(title='Error', message='Please don\'t leave the email field empty!')
        return False

    password = password_entry.get()

    if not password:
        tkinter.messagebox.showwarning(title='Error', message='Please don\'t leave the password field empty!')
        return False

    message = f'These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?'
    is_ok = tkinter.messagebox.askokcancel(title=website, message=message)

    if is_ok:

        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

        to_save = ' | '.join((website, email, password))
        with open('./Day 29 - Intermediate - Password Manager/data.txt', 'a') as file:
            file.write(to_save + '\n')

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='white')

canvas = tkinter.Canvas(width=200, height=200, bg='white', highlightthickness=0)
image = tkinter.PhotoImage(file='./Day 29 - Intermediate - Password Manager/logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text='Website:', bg='white')
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text='Email/Username:', bg='white')
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=34)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=34)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'kevin.mrosa96@gmail.com')

password_entry = tkinter.Entry(width=24)
password_entry.grid(column=1, row=3, sticky='e')

# Buttons
generate_button = tkinter.Button(text='Generate Password', command=generate)
generate_button.grid(column=2, row=3, sticky='w')

add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='e')

window.mainloop()
