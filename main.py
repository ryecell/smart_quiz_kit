from utilities.smart_quiz_kit_quiz_creator_in_oop_format import (greeting,quizbuilder)
from utilities.smart_quiz_kit_quiz_answer_in_oop_format import(quiz_taker)

user_name = input("Name: ")
greet = greeting(user_name)
greet.hello()


class option:
    def __init__(self):
        self.choice = ""
    
    def choices(self):
        while True:
            try:
                self.choice = int(input())
                if self.choice == 1:
                    create = quizbuilder()
                    create.start_quiz_creation()
                elif self.choice == 2:
                    answer = quiz_taker()
                    answer.take_quiz()
                else:
                    print("The options are only 1 or 2")
                    
            except ValueError:
                print("Error! Please enter either 1 or 2")

project = option()
project.choices()
