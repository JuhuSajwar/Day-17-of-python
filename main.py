from data import *
from quiz_brain import *

class Questions:
    def __init__(self,text , answer):
        self.text = text
        self.answer = answer
        
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text , question_answer)
    question_bank.append(new_question)   
    
quiz = QuizBrain(question_bank)
quiz.next_question() 

while quiz.still_have_question():
    quiz.next_question()           
         