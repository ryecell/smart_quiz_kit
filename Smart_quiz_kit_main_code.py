#function that creates quizzes
def create_quiz():
    subject = input("Enter the subject of your quiz: ")
    
    #function so that the user should input a proper number
    while True:
        try:
            items_total = int(input("How many items will your quiz have?: "))
            if items_total <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        quiz_data = [] #list to store questions
        
    #question and answer input        
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