from utilities.smart_quiz_kit_quiz_creator_in_oop_format import (greeting,quizbuilder)
user_name = input("Name: ")
greet = greeting(user_name)
greet.hello()
mode = int(input())

class option:
    def __init__(self,choice):
        self.choice = choice
    
    def choices(self):
        try:
            if self.choice == 1:
                quiz = quizbuilder()
                quiz.start_quiz_creation()
        except ValueError or int (not (1 and 2)):
            print("Error! Please enter either 1 or 2")

project = option(mode)
project.choices()
