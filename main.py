from turtle import width
import customtkinter as ctk
from components.header import Header
from components.orders import Orders
from components.products import Products
from constants import constants

# https://pyinstaller.org/en/stable/ --> https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging
# https://dribbble.com/shots/16007029-Finance-Dashboard-Design
# pip3 install customtkinter
# https://github.com/TomSchimansky/CustomTkinter/wiki

class App(ctk.CTk):
    def __init__(self): 
        super().__init__()

        self.title("Management System")
        self.calculateCenter()
        self.initUI()

        self.bind('<Escape>', self.escape) # End the program when pressing ESC
    

    def initUI(self):
        # Create the layout for the User Interface
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create the header
        self.header_frame = Header(self)
        self.header_frame.configure(corner_radius=0, fg_color="#415A77", bg_color="#415A77", height=constants["height"] * 0.1)
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        # Create the body
        self.body_frame = ctk.CTkFrame(master=self)
        self.body_frame.configure(corner_radius=0, fg_color="white", bg_color="white")
        self.body_frame.grid(row=1, column=0, sticky="nsew")

        self.body_frame.grid_columnconfigure(1, weight=1)
        self.body_frame.grid_rowconfigure(0, weight=1)

        # Create the Product frame at the left side
        self.products_frame = Products(self.body_frame)
        self.products_frame.configure(corner_radius=0, fg_color="#0D1B2A", bg_color="#0D1B2A", width=constants["width"] * 0.7)
        self.products_frame.grid(row=0, column=0, sticky="nsew")

        # Create the Product frame at the right side
        self.orders_frame = Orders(self.body_frame)
        self.orders_frame.configure(corner_radius=0, fg_color="#1B263B", bg_color="#1B263B")
        self.orders_frame.grid(row=0, column=1, sticky="nsew")
        

    def calculateCenter(self):
        # Allow to place the window in the center of the screen
        x = (self.winfo_screenwidth()/2) - (constants["width"]/2)
        y = (self.winfo_screenheight()/2) - (constants["height"]/2)
        self.geometry('%dx%d+%d+%d' % (constants["width"], constants["height"], x, y))
        self.resizable(False, False)


    def escape(self, event):
        self.destroy()
        

if __name__ == '__main__':
    app = App()
    app.mainloop()