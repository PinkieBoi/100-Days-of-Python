import asyncio
from trivia import trivia
from quiz_brain import QuizBrain
from question_model import Question

loop = asyncio.get_event_loop()
questions = loop.run_until_complete(trivia.question(amount=15, category=1, quizType='boolean'))

question_bank = []
for item in questions:
    new_q = Question(item['question'], item['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
