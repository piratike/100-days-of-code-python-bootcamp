# Code for Day 17 Project

# Import needed classes and data
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

# Create the questions list
question_bank = list()

for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz!')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')
