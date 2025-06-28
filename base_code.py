#abstract class
from abc import ABC, abstractmethod

class BaseQuiz(ABC):
    def __init__(self,root,go_home):
        self.root = root
        self.go_home = go_home

    def clear(self):
        for widget in self.root.winfo.children():
            widget.destroy()
    
    def run(self):
        """Start the quiz"""
        pass