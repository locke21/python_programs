from question_model import Question
from data import TriviaData
from quiz_brain import QuizBrain
from ui import QuizInterface


triviadata = TriviaData()
question_bank = []
question_category = triviadata.question_data[0]['category']
for question in triviadata.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz, question_category)

