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
