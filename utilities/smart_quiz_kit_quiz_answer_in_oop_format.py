class quiz_taker:
    def __init__(self):
        self.subject = ""
        self.questions = []
        self.score = 0
    
    def answer_quiz(self,section):
        section = input("Enter your section: ")
        print("Enter the subject of your quiz")
        self.subject = input()
        try:
            quiz_subject = self.subject + "quiz.txt"
            with open(quiz_subject, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("File not found")
            return False
        
        counter = 0
        while counter < len(lines):
            line = lines[counter].strip()
            
            #for heather and empty lines
            if line.startswith("Subject: ") or line.startswith("Total Questions") or line == '':
                counter += 1
                continue
            
            #questions
            if line[0].isdigit() and '.' in line:
                question_text = line[line.find(".") + 1:].strip()
                choices = {}
                counter += 1
                
                while counter < len(lines):
                    choice_line = line[counter].strip()
                    
                    if choice_line.startswith("[Correct answer:"):
                        correct = choice_line.split(":")[1].strip("]")
                        break
                    
                    elif choice_line[0] in "abcd" and choice_line[1] == ".":
                        key = choice_line[0]
                        val = choice_line[3:].strip()
                        choices[key] = val
                
                counter += 1
                
            self.questions.append({
                "question": question_text,
                "choices" : choices,
                "correct" : correct
            })
            
            counter += 1    
        return True

    def take_quiz(self):
        print("\n Starting Quiz...")
        for index, ques in enumerate(self.questions, start = 1):
            print(f"Question {index}: {ques['question']}")
            for key, val in ques['choices'].items():
                print(f"    {key}. {val}")
                
            while True:
                print("Your answer:")
                answer = input().lower()
                if answer in ques['choices']:
                    break
                print("Options a-d only!")
                
            if answer == ques['correct']:
                print('Correct!')
                self.score += 1
            else:
                print("Incorrect")
                
                
        print(f"Quiz Completed! Your score: {self.score}/{len(self.questions)}\n")