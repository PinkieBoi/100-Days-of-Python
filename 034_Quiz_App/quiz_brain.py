import html


class QuizBrain:
    def __init__(self, questions):
        self.quiz_data = questions
        self.asked = 0
        self.score = 0
        self.current_question = None

    def check_answer(self, question, response):
        """Checks if user is correct and increments score"""
        if response == question.answer:
            self.score += 1
            return True

    def next_question(self):
        """Asks current question & returns user response"""
        self.current_question = self.quiz_data[self.asked]
        self.asked += 1
        return html.unescape(self.current_question.question)

    def still_has_questions(self):
        return self.asked < len(self.quiz_data)
