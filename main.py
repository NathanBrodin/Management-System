import customtkinter as ctk
from components.header import Header
from components.orders import Orders
from components.products import Products
from constants import constants

# https://pyinstaller.org/en/stable/
# https://dribbble.com/shots/16007029-Finance-Dashboard-Design
# pip3 install customtkinter

class App:
    def __init__(self, root):
        self.root = root
        root.title("Management System")

        self.calculateCenter(root)
        self.initUI(root)

        root.bind('<Escape>', self.escape) # End the program when pressing ESC

        root.mainloop()
    
    def initUI(self, root):
        root.configure(bg=constants["bg_color"])

        header = Header(root)
        products = Products(root)
        orders = Orders(root)
        

    def calculateCenter(self, root):
        # Allow to place the window in the center of the screen
        x = (root.winfo_screenwidth()/2) - (constants["width"]/2)
        y = (root.winfo_screenheight()/2) - (constants["height"]/2)
        root.geometry('%dx%d+%d+%d' % (constants["width"], constants["height"], x, y))
        root.resizable(False, False)

    def escape(self, event):
        self.root.destroy()
        

if __name__ == '__main__':
    ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    root = ctk.CTk()
    app = App(root)