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
    question = ''
    choices = {}
    correct_answer = ''
    state = 'reading'
    
    for line in lines:
        line = line.strip()
        #checks if the line is a question or no
        if line.startswith("Subject") or line.startswith("Total Questions:") or line == '':
            continue
        
        #prints question if the line starts with a number
        if line[0].isdigit and '.' in line:
            if question:
                print(f"\n{question}")
                for key, val in choices.items():
                    print(f"    {key}. {val}")
                    while True:
                        student_answer =  input("Your answer(a-d): ").lower()
                        if student_answer in choices:
                            break
                        else:
                            print("Invalid answer. Please choose a, b, c, or d.")
                    if student_answer == correct_answer:
                        score += 1
                    else:
                        pass
                    total_questions += 1
                    question = ""
                    choices = {}
                
                    
