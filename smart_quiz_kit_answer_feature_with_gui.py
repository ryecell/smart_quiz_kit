import tkinter as tk
from tkinter import messagebox, filedialog

class QuizTaker:
    def __init__(self, root, go_home):
        self.root = root
        self.go_home = go_home
        self.questions = []
        self.index = 0
        self.score = 0
        self.selected = tk.StringVar()
        self.load_quiz()
        
    def open_file(self, path):
            try:
                with open(path) as f:
                    lines = f.readlines()
            except:
                return False

            self.questions = []
            self.index = 0
            self.score = 0
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if not line or line.startswith("Subject") or line.startswith("Total"):
                    i += 1
                    continue
                if line[0].isdigit():
                    q_text = line.split(".", 1)[1].strip()
                    choices = {}
                    i += 1
                    while i < len(lines):
                        if lines[i].strip().startswith("[Correct answer:"):
                            correct = lines[i].strip().split(":")[1].strip(" ]")
                            break
                        elif lines[i].strip()[0] in "abcd":
                            k = lines[i].strip()[0]
                            v = lines[i].strip()[3:]
                            choices[k] = v
                        i += 1
                    self.questions.append({"question": q_text, "choices": choices, "correct": correct})
                i += 1
            return bool(self.questions)
        
    def show_question(self):
        self.clear()
        if self.index >= len(self.questions):
            return self.show_result()

        q = self.questions[self.index]
        self.selected.set(None)
        tk.Label(self.root, text=f"Q{self.index + 1}: {q['question']}", font=("Arial", 14), wraplength=450).pack(pady=20)

        for k, v in q["choices"].items():
            tk.Radiobutton(self.root, text=f"{k}. {v}", variable=self.selected, value=k).pack(anchor="w", padx=40)

        tk.Button(self.root, text="Submit", command=self.submit_answer).pack(pady=20)
        
    def submit_answer(self):
        ans = self.selected.get()
        if not ans:
            messagebox.showwarning("Required", "Please choose an answer.")
            return
        if ans == self.questions[self.index]["correct"]:
            self.score += 1
        self.index += 1
        self.show_question()

    def show_result(self):
        self.clear()
        tk.Label(self.root, text="✅ Quiz Completed!", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Score: {self.score} / {len(self.questions)}", font=("Arial", 14)).pack()
        tk.Button(self.root, text="Back to Home", command=self.go_home).pack(pady=10)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
