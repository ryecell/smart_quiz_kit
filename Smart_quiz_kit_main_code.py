#function that creates quizzes
def create_quiz():
    subject = input("Enter the subject of your quiz: ")
    items_total = int(input("How many items will your quiz have?: "))
    items_counter = 0
    
    while items_counter < items_total:
        question = input(f"{items_counter + 1}.")
        a = input("a. ")
        b = input("b. ")
        c = input("c. ")
        d = input("d. ")
        correct_answer = input("Correct answer: ")
        
        items_counter += 1

        