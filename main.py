from smart_quiz_kit_answer_feature_with_gui import QuizTaker
from smart_quiz_kit_create_feature_with_gui import QuizCreator
import tkinter as tk
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x500")
        self.main_menu()

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text="📘 Quiz Application", font=("Arial", 18)).pack(pady=30)
        tk.Button(self.root, text="Create Quiz (Teacher)", width=30, command=self.create_mode).pack(pady=10)
        tk.Button(self.root, text="Take Quiz (Student)", width=30, command=self.take_mode).pack(pady=10)
        tk.Button(self.root, text="Exit", width=30, command=self.root.quit).pack(pady=10)

    def create_mode(self):
        self.clear()
        creator = QuizCreator(self.root, self.main_menu)
        creator.run()  # POLYMORPHIC CALL

    def take_mode(self):
        self.clear()
        taker = QuizTaker(self.root, self.main_menu)
        taker.run()  # POLYMORPHIC CALL

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

