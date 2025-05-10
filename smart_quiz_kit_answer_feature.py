def answer_quiz():

#enter student info
    student_name = input("Enter your full name (LN, FN MI.): ")
    section = input("Enter your section(ex. BSCPE 1-2): ")
    subject = input("Enter the subject you want to answer: ")

    file_path = subject +'_quiz.txt' 
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {subject} does not exist")

    score = 0
    total_questions = 0
    amount= 0
    while line < len(lines):
        line = lines[amount].strip()
        
        #function to skip empty lines and non question lines
        if line.startswith("Subjecet:") or line.startswith("Total Questions:") or line == "":
            line += 1
            continue
        
        #start of questino
        if line[0].isdigit and '.' in line:
            question = line[line.find(".") + 1:].strip()
            choices = {}
            amount += 1
            
            while amount < len(lines):
                choice_line = line[amount].strip()
                if choice_line.startswith("[Correct answer:"):
                    correct_answer = choice_line.split(":")[1].strip("]")
                    amount += 1
                    break
                elif choice_line[0] in "abcd" and choice_line[1] == ".":
                    key = choice_line[0]
                    val = choice_line[3:]
                    choices[key] = val
                amount += 1
            
             #printing the questions
            print(f"\n Question {total_questions}: {question}")
            for key, val in choices.items():
                print(f"{key}. {val}")
            
                
answer_quiz()
