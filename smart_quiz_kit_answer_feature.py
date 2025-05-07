#enter student info
student_name = input("Enter your full name (LN, FN MI.): ")
section = input("Enter your section(ex. BSCPE 1-2): ")
subject = input("Enter the subject you want to answer: ")

file_path = subject +'_quiz.txt' 
try:
    file = open(file_path, 'r')
    
    lines = file.readlines(5)
    for line in lines:
        print(line.strip())
        
except FileNotFoundError:
    print(f"Error: Subject does not exist")
    print(file_path)

score = 0
