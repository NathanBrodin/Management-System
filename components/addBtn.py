from turtle import width
import customtkinter as ctk
from constants import constants

class AddBtn(ctk.CTkButton):
    def __init__(self, text="", command_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text=text, command=command_name,fg_color="#b4eeb4", corner_radius=constants["width"] * 0.01, text_color="black", width=10)