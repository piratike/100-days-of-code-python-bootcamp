# Code for Day 34 Project

import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'

class Interface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = tkinter.Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Question Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some question',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_img = tkinter.PhotoImage(file='./Day 34 - Intermediate+ - GUI Quiz App/images/true.png')
        self.true_button = tkinter.Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_img = tkinter.PhotoImage(file='./Day 34 - Intermediate+ - GUI Quiz App/images/false.png')
        self.false_button = tkinter.Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Put first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # Prints in the interface a new question

        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)

        else:

            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question, text='You\'ve reached the end of the quiz.')
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Gives a True from the user to the question in screen

        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        # Gives a False from the user to the question in screen

        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        # Gives feedback to the user changing the color of the question container

        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
