from utilities.smart_quiz_kit_quiz_creator_in_oop_format import (greeting,quizbuilder)
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
                    quiz = quizbuilder()
                    quiz.start_quiz_creation()
                else:
                    print("The options are only 1 or 2")
            except ValueError:
                print("Error! Please enter either 1 or 2")

project = option()
project.choices()
