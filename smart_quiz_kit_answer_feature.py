
def answer_quiz():

#enter student info
    file_path = subject +'_quiz.txt' 
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {subject} does not exist")

    score = 0
    total_questions = 0
    amount= 0
    while amount < len(lines):
        line = lines[amount].strip()
        
        #function to skip empty lines and non question lines
        if line.startswith("Subjecet:") or line.startswith("Total Questions:") or line == "":
            amount += 1
            continue
        
        #start of questino
        if line[0].isdigit and '.' in line:
            question = line[line.find(".") + 1:].strip()
            choices = {}
            amount += 1
            
            while amount < len(lines):
                choice_line = lines[amount].strip()
                if choice_line.startswith("[Correct answer:"):
                    correct_answer = choice_line.split(":")[1].strip("]")
                    amount += 1
                    break
                elif choice_line[0] in "abcd" and choice_line[1] == ".":
                    key = choice_line[0]
                    val = choice_line[2:]
                    choices[key] = val
                amount += 1
            
            #printing the questions
            print(f"\nQuestion {total_questions + 1}: {question}")
            for key, val in choices.items():
                print(f"{key}. {val}")
            
            #user answer
            while True:
                user_answer = input("What is your answer? (a-d): ")
                if user_answer in choices:
                    break
                else:
                    print("Please enter a valid option!")
            
            total_questions += 1
        else:
            amount += 1

    print("Quiz Completed!")
    

student_name = input("Enter your full name (LN, FN MI.): ")
section = input("Enter your section(ex. BSCPE 1-2): ")
subject = input("Enter the subject you want to answer: ")              
answer_quiz()
