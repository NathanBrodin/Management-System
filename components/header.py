import customtkinter as ctk
from constants import constants

class Header(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header_title = ctk.CTkLabel(master=self, text="Management System", text_font=("Roboto Medium", -16))
        self.header_title.grid(row=0, column=0, pady=0, padx=10)

        self.header_subtitle = ctk.CTkLabel(master=self, text="Created by Nathan Brodin", text_font=("Roboto", -12))
        self.header_subtitle.grid(row=1, column=0, pady=0, padx=10)