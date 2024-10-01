import requests
from ui import QuizInterface
from quiz_brain import QuizBrain
from question_model import Question

params = {
    "amount": 20,
    "category": 9,
    "type": "boolean"
}

questions = requests.get(url="https://opentdb.com/api.php", params=params).json()
question_bank = []
for item in questions["results"]:
    new_q = Question(item['question'], item['correct_answer'])
    question_bank.append(new_q)
quiz = QuizBrain(question_bank)
interface = QuizInterface(quiz)
