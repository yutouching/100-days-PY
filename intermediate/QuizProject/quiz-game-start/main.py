from data import question_data
from question_model import Question, QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    answer_text = question['answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()     #check 已经包含在next的函数中


print(f'You have completed all the quiz.\n The final score is {quiz.score/quiz.question_number}')

