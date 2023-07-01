from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_bank = []
for i in question_data:
    q_text = i['text']
    q_ans = i['answer']
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)
# quiz.user_input()
while quiz.still_has_question():
    a = quiz.user_input()

print(f"Your Score is: {quiz.score}/{quiz.question_number}")