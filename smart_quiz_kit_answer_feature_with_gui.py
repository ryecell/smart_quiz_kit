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
        
        