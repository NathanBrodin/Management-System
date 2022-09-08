import tkinter as tk

class AddBtn:
    def __init__(self, root, text, command):
        self.btn = tk.Button(root, text=text, command=command)
        self.btn.pack()