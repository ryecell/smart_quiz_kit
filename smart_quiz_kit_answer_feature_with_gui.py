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