import customtkinter as ctk
from constants import constants

class Header(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = ctk.CTkLabel(master=self, text="Management System", text_font=("Roboto Medium", -16))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        self.subtitle = ctk.CTkLabel(master=self, text="Created by Nathan Brodin", text_font=("Roboto", -12))
        self.subtitle.grid(row=1, column=0, pady=0, padx=10)