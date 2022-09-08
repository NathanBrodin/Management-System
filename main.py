import tkinter as tk
from components.header import Header
from components.orders import Orders
from components.products import Products

# https://pyinstaller.org/en/stable/
# https://dribbble.com/shots/16007029-Finance-Dashboard-Design

class App:
    def __init__(self, root):
        self.root = root
        root.title("Management System")

        self.calculateCenter(root)
        self.initUI(root)

        root.bind('<Escape>', self.escape) # End the program when pressing ESC

        root.mainloop()
    
    def initUI(self, root):
        root.configure(bg='#FFFFFF')

        header = Header(root)
        products = Products(root)
        orders = Orders(root)
        

    def calculateCenter(self, root):
        # Allow to place the window in the center of the screen
        w = 800
        h = 500
        x = (root.winfo_screenwidth()/2) - (w/2)
        y = (root.winfo_screenheight()/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(False, False)

    def escape(self, event):
        self.root.destroy()
        

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)

# import tkinter as tk
# from tkextrafont import Font

# window = tk.Tk()
# font = Font(file="tests/overhaul.ttf", family="Overhaul")
# tk.Label(window, text="Hello", font=font).pack()
# window.mainloop()