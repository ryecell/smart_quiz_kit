class quiz_taker:
    def __init__(self):
        self.subject = ""
        self.questions = []
        self.score = 0
    
    def answer_quiz(self):
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
                
            
        
    
        