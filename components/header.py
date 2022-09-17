import customtkinter as ctk
from constants import constants

class Header(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.header_title = ctk.CTkLabel(master=self, text="Management System", text_font=("Arial Black", 16))
        self.header_title.grid(row=0, column=0, pady=0, padx=10, sticky="nsew")

        self.header_subtitle = ctk.CTkLabel(master=self, text="Created by Nathan Brodin", text_font=("Arial", 12), text_color="#a6a6a7")
        self.header_subtitle.grid(row=1, column=0, pady=0, padx=0, sticky="nsew")