class QuizBrain:
    def __init__(self, questions):
        self.quiz_data = questions
        self.asked = 0
        self.score = 0

    def check_answer(self, question, response):
        """Checks if user is correct and increments score"""
        if response == question.answer:
            self.score += 1
            print("Correct!")
        print(f"The correct answer was: {question.answer}\n"
              f"Your current score is {self.score}/{self.asked}")

    def next_question(self):
        """Asks current question & returns user response"""
        current_question = self.quiz_data[self.asked]
        self.asked += 1
        response = input(f"Q{self.asked}. {current_question.question}\n True or False: ").capitalize()
        self.check_answer(current_question, response)

    def still_has_questions(self):
        return self.asked < len(self.quiz_data)
