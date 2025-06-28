import tkinter as tk
from tkinter import messagebox, filedialog
from base_code import BaseQuiz

class QuizCreator(BaseQuiz):
    def __init__(self, root, go_home):
        super().__init__(root, go_home)
        self.questions = []
        self.current = 0

    def run(self):
        self.start_screen()


    def start_screen(self):
        tk.Label(self.root, text="Create Quiz", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Subject:").pack()
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.pack()

        tk.Label(self.root, text="Total Questions:").pack()
        self.total_entry = tk.Entry(self.root)
        self.total_entry.pack()

        tk.Button(self.root, text="Start", command=self.setup_questions).pack(pady=10)

    def setup_questions(self):
        try:
            self.subject = self.subject_entry.get()
            self.total = int(self.total_entry.get())
            if not self.subject or self.total <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Valid subject and question count required.")
            return
        self.questions = []
        self.current = 0
        self.next_question()

    def next_question(self):
            self.clear()
            tk.Label(self.root, text=f"Question {self.current + 1}", font=("Arial", 14)).pack(pady=10)
            self.q_entry = tk.Entry(self.root, width=50)
            self.q_entry.pack(pady=5)
            self.choices = {}
            for key in "abcd":
                tk.Label(self.root, text=f"Choice {key}:").pack()
                self.choices[key] = tk.Entry(self.root, width=40)
                self.choices[key].pack()
            tk.Label(self.root, text="Correct Answer (a–d):").pack()
            self.correct = tk.Entry(self.root)
            self.correct.pack()
            tk.Button(self.root, text="Next", command=self.save_question).pack(pady=10)

