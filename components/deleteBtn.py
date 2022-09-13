import customtkinter as ctk

class DeleteBtn(ctk.CTkButton):
    def __init__(self, text, command, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text=text, command=command, bg_color="#b11540", fg_color="#b11540")