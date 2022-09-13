from turtle import width
import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 
import json

class Products(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()
    
        return
        self.loadProducts()

        apple = Product(root, "21353", "Apple", 1.3, 10)
        banana = Product(root, "21354", "Banana", 1.5, 20)
        orange = Product(root, "21355", "Orange", 1.7, 30)

        AddBtn(root, "Add new product", self.addProduct("21356", "Pineapple", 2.3, 40))
        DeleteBtn(root, "Delete product", self.deleteProduct)

    def initUI(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.product_list_frame = ctk.CTkFrame(master=self)
        self.product_list_frame.configure(corner_radius=0, fg_color="red", bg_color="red", width=constants["width"] * 0.7, height=constants["height"] * 0.8)
        self.product_list_frame.grid(row=0, column=0, sticky="nsew")

        self.product_list_frame_title = ctk.CTkLabel(master=self.product_list_frame, text="Products available")
        self.product_list_frame_title.grid(row=0, column=0, sticky="nsew")

        #self.test_product = self.Product(self.product_list_frame, product_id="00001", product_name="Apple", product_price="1.3", product_stock="5")
        #self.test_product.grid(row=0, column=0, sticky="nsew")

        self.configure_frame = ctk.CTkFrame(master=self)
        self.configure_frame.configure(corner_radius=0, fg_color="blue", bg_color="blue")
        self.configure_frame.grid(row=1, column=0, sticky="nsew")

        self.addBtn = AddBtn(text="Add new product", command=self.addProduct, master=self.configure_frame)
        self.deleteBtn = DeleteBtn(text="Delete product", command=self.deleteProduct, master=self.configure_frame)
        self.addBtn.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")
        self.deleteBtn.grid(row=1, column=1, pady=10, padx=20, sticky="nsew")

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
            self.configure(corner_radius=5, fg_color="green", bg_color="green", width=constants["width"] * 0.01, height=constants["height"] * 0.01)

            return
            self.product_id_label = ctk.CTkLabel(master=self, text=self.product_id)
            self.product_name_label = ctk.CTkLabel(master=self, text=self.product_name)
            self.product_price_label = ctk.CTkLabel(master=self, text=self.product_price + "€")
            self.product_stock_label = ctk.CTkLabel(master=self, text=self.product_stock + "pcs")

            self.product_id_label.grid(row=0, column=0, pady=10, padx=0)
            self.product_name_label.grid(row=1, column=0, pady=10, padx=0)
            self.product_price_label.grid(row=2, column=0, pady=10, padx=0)
            self.product_stock_label.grid(row=3, column=0, pady=10, padx=0)
            