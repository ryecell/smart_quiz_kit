#function that creates quizzes
def create_quiz():
    subject = input("Enter the subject of your quiz: ")
    items_total = int(input("How many items will your quiz have?: "))
    items_counter = 0
    quiz_data = [] #list to store questions
    
    while items_counter < items_total:
        question = input("Enter question.\nQuestion "f"{items_counter + 1}. ")
        alphabets = [chr(i) for i in range(97, 101)] # -> letters a-b loop
        
        #choices loop for a,b,c,d
        choices = {} 
        for letters in alphabets:
            choices[letters] = input(f"Choice {letters}: ")
            
        correct_answer = input("Correct answer(a-d): ")
        
        items_counter += 1
        
        #dictionary to store values
        question_data = {
            "Question": question,
            "Choices": choices,
            "Correct answer": correct_answer
        }
        
create_quiz()