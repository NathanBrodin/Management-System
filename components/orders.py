import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn  
import json

class Orders(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loadOrders()
        self.loadProducts()


        self.initUI()  

    def initUI(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.orders_list_frame = ctk.CTkFrame(master=self)
        self.orders_list_frame.configure(corner_radius=0, fg_color="black")
        self.orders_list_frame.grid(row=0, column=0, sticky="nsew")

        self.orders_list_frame_title = ctk.CTkLabel(master=self, text="Orders activity",  width=120, height=25, text_font=("Arial Black", 12), text_color="white", anchor="nw")
        self.orders_list_frame_title.grid(row=0, column=0,  pady=10, padx=10, sticky="nsew")

        self.configure_frame = ctk.CTkFrame(master=self)
        self.configure_frame.configure(corner_radius=0, fg_color="black")
        self.configure_frame.grid(row=1, column=0, sticky="nsew")

        self.createBtn = AddBtn(text="Create new order", command_name=self.createOrder, master=self.configure_frame)
        self.cancelBtn = DeleteBtn(text="Cancel order", command_name=self.cancelOrder, master=self.configure_frame)
        self.createBtn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.cancelBtn.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        self.orders_list = []
        i = 0
        self.orders = self.orders_available_from_file["orders"]
        for order in self.orders:
            if i == 9:
                break
            for key, value in order.items():
                self.orders_list.append(self.Order(self.orders_list_frame, product_id=key, product_name=value["product_name"], product_price=str(value["product_price"]), product_stock=str(value["product_stock"])))
                self.orders_list[i].grid(column=0, row=i, pady=10, padx=10, sticky="nsew")

                i += 1

    def loadOrders(self):
        pass

    def loadProducts(self):
        with open('./src/products.json') as json_products:
            try :
                data = json.load(json_products)
            except:
                print("Error loading products")
                return

        self.products_available_from_file = data
        self.products_available = self.products_available_from_file["products_available"]

    def createOrder(self):
        self.create_window = ctk.CTkToplevel()
        self.create_window.title("Create a new order")
        self.create_window.geometry("400x400")

        products_names = []
        for product in self.products_available:
            for key, value in product.items():
                products_names.append(value["product_name"])
        
        self.combobox = ctk.CTkOptionMenu(master=self.create_window, values=products_names)  
        self.combobox.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Select quantity
        # if quantity > stock -> error

        # Select customer name

    def cancelOrder(self):
        pass



    class Order(ctk.CTkFrame):
        def __init__(self, *args, order_product, order_quantity, order_id, order_status, order_date, **kwargs):
            super().__init__(*args, **kwargs)

            self.order_product = order_product
            self.order_quantity = order_quantity
            self.order_id = order_id
            self.order_status = order_status
            self.order_cost = int(order_quantity) * int(order_product["product_price"])
            self.order_date = order_date

            self.initUI()

        def initUI(self):
            self.configure(corner_radius=constants["width"] * 0.02, fg_color="#ffefe3",  width=0, height=0)
            self.grid(padx=5, pady=5, sticky="nsew")

            self.order_customer = ctk.CTkLabel(master=self, text="", text_font=("Arial Black", 14), text_color="black", anchor="w", width=0)