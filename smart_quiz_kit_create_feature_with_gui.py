import tkinter as tk
from tkinter import messagebox, filedialog

class QuizCreator:
    def __init__(self, root, go_home):
        self.root = root
        self.go_home = go_home
        self.questions = []
        self.current = 0
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
