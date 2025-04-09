#function that creates quizzes
def create_quiz():
    subject = input("Enter the subject of your quiz: ")
    items_counter = 0
    quiz_data = [] #list to store questions
    
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
            
    #question and answer input        
    while items_counter < items_total:
        question = input("Enter question.\nQuestion "f"{items_counter + 1}. ")
        alphabets = [chr(i) for i in range(97, 101)] # -> letters a-b loop
        
        #choices loop for a,b,c,d
        choices = {} 
        for letters in alphabets:
            choices[letters] = input(f"Choice {letters}: ")
            
        correct_answer = input("Correct answer(a-d): ")

        #dictionary to store values
        question_data = {
            "Question": question,
            "Choices": choices,
            "Correct answer": correct_answer
        }
        
        quiz_data.append(question_data)
        items_counter += 1
        
    #saving to a txt file
    filename = f"{subject.lower().replace(' ', '_')}_quiz.txt"
    
    with open(filename, "w") as file:
        file.write(f"Subject: {subject}\n")
        file.write(f"Total Questions: {items_total}\n------------------------\n")
        for i, questions in enumerate(quiz_data, start = 1):
            file.write(f"{i}.{questions['Question']}\n")
            for key, val in questions["Choices"].items():
                file.write(f"   {key}.{val}\n")
            file.write(f"   [Correct answer: {questions["Correct answer"]}]\n\n")
    print(f"\n✅ Quiz saved successfully to '{filename}'!")

create_quiz()