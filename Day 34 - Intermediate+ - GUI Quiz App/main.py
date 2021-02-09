# Code for Day 34 Project, from Day 17

# Import needed classes and data
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from ui import Interface

# Create the questions list
question_bank = list()

for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)
ui = Interface(quiz)
