# Code for Day 28 Project

import tkinter, math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_clicked():

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checks_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_clicked():

    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text='Break', fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text='Break', fg=PINK)

    else:
        count_down(work_seconds)
        title_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_clicked()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

checks_label = tkinter.Label(text='', font=(FONT_NAME, 12, 'bold'), bg=YELLOW, fg=GREEN)
checks_label.grid(column=1, row=2, pady=20)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file='./Day 28 - Intermediate - Pomodoro/tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text='Start', command=start_clicked, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', command=reset_clicked, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
