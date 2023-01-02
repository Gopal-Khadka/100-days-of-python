import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        self.correct_answer = current_question.answer
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(
        self,
        guess,
    ):
        if self.correct_answer == str(guess):
            self.score += 1
            return True
        else:
            return False
