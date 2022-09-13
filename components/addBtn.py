import customtkinter as ctk

class AddBtn(ctk.CTkButton):
    def __init__(self, text, command, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text=text, command=command, bg_color="#b4eeb4", fg_color="#b4eeb4")