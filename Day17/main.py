from pprint import pprint

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_back = []

for a in question_data:
    question = Question(a['text'], a['answer'])
    question_back.append(question)

quiz = QuizBrain(question_back)
CorrectCount = quiz.QuestionTime()

print(f"You answered this many Questions correctly::{CorrectCount}/{len(question_back)}")
