from tkinter import *

class Window: 
    def __init__(self, window): 
        self.window = window

        self.window_width = window.winfo_screenwidth()
        self.window_height = window.winfo_screenheight()

        