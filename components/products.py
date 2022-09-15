from turtle import width
import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 
import json

class Products(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loadProducts()
        self.initUI()

    def initUI(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.product_list_frame = ctk.CTkFrame(master=self)
        self.product_list_frame.configure(corner_radius=0, fg_color="white")
        self.product_list_frame.grid(row=0, column=0, sticky="nsew")

        self.product_list_frame_title = ctk.CTkLabel(master=self.product_list_frame, text="Products available",  width=120, height=25, text_font=("Arial Black", 12), text_color="black")
        self.product_list_frame_title.grid(row=0, column=0,  pady=10, padx=10, sticky="nsew")

        ############################# TEST #############################

        self.test_product = self.Product(self.product_list_frame, product_id="00001", product_name="Apple", product_price="1.3", product_stock="5")
        self.test_product.grid(row=1, column=0, sticky="nsew")

        self.test_product = self.Product(self.product_list_frame, product_id="00002", product_name="Banana", product_price="0.89", product_stock="12")
        self.test_product.grid(row=1, column=1, sticky="nsew")

        self.test_product = self.Product(self.product_list_frame, product_id="00003", product_name="Strawberry", product_price="2.45", product_stock="45")
        self.test_product.grid(row=2, column=0, sticky="nsew")

        ################################################################

        self.configure_frame = ctk.CTkFrame(master=self)
        self.configure_frame.configure(corner_radius=0, fg_color="white")
        self.configure_frame.grid(row=1, column=0, sticky="nsew")

        self.addBtn = AddBtn(text="Add new product", command=self.addProduct, master=self.configure_frame)
        self.deleteBtn = DeleteBtn(text="Delete product", command=self.deleteProduct, master=self.configure_frame)
        self.addBtn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.deleteBtn.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

    def addProduct(self, product_id, product_name, product_price, product_stock):
        new_product = {
            product_id : {
                "product_name": product_name,
                "product_price": product_price,
                "product_stock": product_stock
            }
        }

        self.products_available_from_file["products_available"].append(new_product)
        with open("./src/products.json", "w") as products_file:
            json.dump(self.products_available_from_file, products_file, indent=4)

        print("New product added")
    
    def deleteProduct(self):
        print("Product deleted")

    def loadProducts(self):
        with open('./src/products.json') as json_products:
            try :
                data = json.load(json_products)
                print("Products loaded")
            except:
                print("Error loading products")
                return

        self.products_available_from_file = data

    class Product(ctk.CTkFrame):
        def __init__(self, *args, product_id="", product_name="", product_price="", product_stock="", **kwargs):
            super().__init__(*args, **kwargs)
            
            self.product_id = product_id
            self.product_name = product_name
            self.product_price = product_price
            self.product_stock = product_stock

            self.initUI()

        def initUI(self):
            self.configure(corner_radius=constants["width"] * 0.02, fg_color="#ffefe3", width=constants["width"] * 0.005, height=constants["height"] * 0.005)
            self.grid(padx=10, pady=10)

            self.product_name_label = ctk.CTkLabel(master=self, text=self.product_name, text_font=("Arial Black", 14), text_color="black")
            self.product_id_label = ctk.CTkLabel(master=self, text="#" + self.product_id, text_font=("Arial", 12), text_color="#a6a6a7")
            self.product_price_label = ctk.CTkLabel(master=self, text=self.product_price + "€", text_font=("Arial", 12), text_color="black")
            self.product_stock_label = ctk.CTkLabel(master=self, text=self.product_stock + "pcs", text_font=("Arial", 12), text_color="black")

            self.product_name_label.grid(row=0, column=0, pady=3, padx=0)
            self.product_id_label.grid(row=1, column=0, pady=3, padx=0)
            self.product_price_label.grid(row=2, column=0, pady=3, padx=0)
            self.product_stock_label.grid(row=1, column=1, pady=3, padx=0)
            