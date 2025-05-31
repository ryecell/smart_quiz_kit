class greeting:
    def __init__(self,name):
        self.name = name
        
        
    def hello(self):
        print("Hello", self.name+"!")
        print("What do you wish to do?\n-----------------------")
        print("1. Create a quiz")
        print("2. Answer a quiz")

class quizbuilder:
    def __init__(self):
        self.subject = ""
        self.questions = []

    def start_quiz_creation(self):
        self.subject = input("Enter the subject of your quiz: ")
        while True:
            try:
                total_items = int(input("How many questions will your quiz have?: "))
                if total_items <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number.")

        for i in range(total_items):
            print(f"\nQuestion {i + 1}:")
            question = input("Enter the question: ")

            choices = {}
            for letter in ['a', 'b', 'c', 'd']:
                choice = input(f"  Choice {letter}: ")
                choices[letter] = choice

            while True:
                correct = input("Enter the correct answer (a–d): ").lower()
                if correct in choices:
                    break
                print("Invalid choice❗. Please enter a, b, c, or d.")

            self.questions.append({
                "question": question,
                "choices": choices,
                "correct": correct
            })

        self.save_to_file()

    def save_to_file(self):
        #saving to a txt file
        filename = self.subject.lower().replace(" ","_") + "quiz.txt"
        try:
            with open(filename, "w") as file:
                file.write(f"Subject: {self.subject}\n")
                file.write(f"Total Questions: {len(self.questions)}\n------------------------\n")
                
                for i, questions in enumerate(self.questions, start = 1):
                    file.write(f"{i}.{questions['Question']}\n")
                    for key, val in questions["Choices"].items():
                        file.write(f"   {key}.{val}\n")
                    file.write(f"   [Correct answer: {questions["Correct answer"]}]\n\n")
                    
            print(f"\n✅ Quiz saved successfully to '{filename}'!")
        except Exception as e:
            
            print("Failed to save",e)
            
class option:
    def __init__(self,choice):
        self.choice = choice
    
    def choices(self):
        try:
            if self.choice == 1:
                quizbuilder
        except ValueError or int (not (1 and 2)):
            print("Error! Please enter either 1 or 2")
            