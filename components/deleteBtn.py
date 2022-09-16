import customtkinter as ctk
from constants import constants

class DeleteBtn(ctk.CTkButton):
    def __init__(self, text="", command_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text=text, command=command_name, fg_color="#b11540", corner_radius=constants["width"] * 0.01, text_color="black")