import tkinter as tk
from constants import constants

class Header:
    def __init__(self, root):
        header_frame = tk.Frame(root, bg=constants["frame_color"], width=constants["width"], height=constants["height"]*0.08)
        header_frame.pack()

        title = tk.Label(root, text="Management System")
        title.pack()

        subtitle = tk.Label(root, text="Created by Nathan Brodin")
        subtitle.pack()