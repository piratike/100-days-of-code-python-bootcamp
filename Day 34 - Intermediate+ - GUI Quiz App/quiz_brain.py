import html

class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)

        return f'Q.{self.question_number}: {q_text}'

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False

        else:
            return True

    def check_answer(self, answer):
        correct_answer = self.current_question.answer

        if answer == correct_answer:
            self.score += 1
            return True

        else:
            return False
