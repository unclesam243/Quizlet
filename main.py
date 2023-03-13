"""# create class by typing class "Class":
class User:
    #pass #if you want to skip having to add a function in here
    def __init__(self, user_id, username): #This is a way to create a systematicly/generate some specific code for everytime you call the class
        self.user_id = user_id
        self.username = username
        self.followers = 0
# An attribute is a variable associated with an object or in another word information held by the object
#Attribes are the things that the object HAS
user_1 = User("001", "France")

#A function attached to an object is a method
#Methods are the things that the object DOES"""
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)
#    print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")