from tokenize import Number
from turtle import width
import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 
import json
import random

class Products(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loadProducts()
        self.initUI()

    def initUI(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.product_list_frame = ctk.CTkFrame(master=self)
        self.product_list_frame.configure(corner_radius=0)
        self.product_list_frame.grid(row=0, column=0, sticky="nsew")

        self.product_list_frame_title = ctk.CTkLabel(master=self.product_list_frame, text="Products available",  width=120, height=25, text_font=("Arial Black", 12))
        self.product_list_frame_title.grid(row=0, column=0,  pady=10, padx=10, sticky="w", columnspan=2)

        self.product_list = []
        i = 0
        j = 0
        k = 0
        self.products_available = self.products_available_from_file["products_available"]
        for product in self.products_available:
            if k == 9:
                break
            for key, value in product.items():
                if (i % 3) == 0:
                    j += 1
                    i = 0

                self.product_list.append(self.Product(self.product_list_frame, product_id=key, product_name=value["product_name"], product_price=str(value["product_price"]), product_stock=str(value["product_stock"])))
                self.product_list[k].grid(column=i, row=j, pady=10, padx=10, sticky="nsew")

                k += 1
                i += 1

        self.configure_frame = ctk.CTkFrame(master=self)
        self.configure_frame.configure(corner_radius=0)
        self.configure_frame.grid(row=1, column=0, sticky="nsew")

        self.addBtn = AddBtn(text="Add new product", command_name=self.addProduct, master=self.configure_frame)
        self.deleteBtn = DeleteBtn(text="Delete product", command_name=self.deleteProduct, master=self.configure_frame)
        self.addBtn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.deleteBtn.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

    def loadProducts(self):
        with open('./src/products.json') as json_products:
            try :
                data = json.load(json_products)
            except:
                print("Error loading products")
                return

        self.products_available_from_file = data

    def addProduct(self):
        self.add_window = ctk.CTkToplevel()
        self.add_window.title("Add new product")
        self.add_window.geometry("400x400")

        self.product_name_entry = ctk.CTkEntry(master=self.add_window, placeholder_text="Product name", width=120, height=25, border_width=2, corner_radius=10)
        self.product_name_entry.grid(row=0, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        self.product_price_entry = ctk.CTkEntry(master=self.add_window, placeholder_text="Product price", width=120, height=25, border_width=2, corner_radius=10)
        self.product_price_entry.grid(row=1, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        self.product_stock_entry = ctk.CTkEntry(master=self.add_window, placeholder_text="Product stock", width=120, height=25, border_width=2, corner_radius=10)
        self.product_stock_entry.grid(row=2, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        confirmBtn = AddBtn(text="Confirm", command_name=self.confirm, master=self.add_window)
        cancelBtn = DeleteBtn(text="Cancel", command_name=self.cancel, master=self.add_window)

        confirmBtn.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
        cancelBtn.grid(row=3, column=1, pady=10, padx=10, sticky="nsew")

    def confirm(self):
        product_id = "".join([random.choice("0123456789") for n in range(5)])

        new_product = {
            product_id : {
                "product_name": self.product_name_entry.get(),
                "product_price": self.product_price_entry.get(),
                "product_stock": self.product_stock_entry.get()
            }
        }

        self.products_available_from_file["products_available"].append(new_product)
        with open("./src/products.json", "w") as products_file:
            json.dump(self.products_available_from_file, products_file, indent=4)

        self.loadProducts()
        self.initUI()

        self.add_window.destroy()

    def cancel(self):
        self.add_window.destroy()
    
    def deleteProduct(self):
        self.delete_window = ctk.CTkToplevel()
        self.delete_window.title("Delete a product")
        self.delete_window.geometry("400x400")

        products_names = []
        for product in self.products_available:
            for key, value in product.items():
                products_names.append(value["product_name"])
        
        self.combobox = ctk.CTkOptionMenu(master=self.delete_window, values=products_names)  
        self.combobox.grid(row=0, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        deleteBtn = AddBtn(text="Delete selection", command_name=self.deleteConfirm, master=self.delete_window)
        cancelBtn = DeleteBtn(text="Cancel", command_name=self.deleteCancel, master=self.delete_window)

        deleteBtn.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
        cancelBtn.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")

    def deleteConfirm(self):
        choice = self.combobox.get()

        for product in self.products_available:
            for key, value in product.items():
                if value["product_name"] == choice:
                    self.products_available.remove(product)
        
        with open("./src/products.json", "w") as products_file:
            json.dump(self.products_available_from_file, products_file, indent=4)

        self.loadProducts()
        self.initUI()

        self.delete_window.destroy()

    def deleteCancel(self):
        self.delete_window.destroy()

    class Product(ctk.CTkFrame):
        def __init__(self, *args, product_id="", product_name="", product_price="", product_stock="", **kwargs):
            super().__init__(*args, **kwargs)
            
            self.product_id = product_id
            self.product_name = product_name
            self.product_price = product_price
            self.product_stock = product_stock

            self.initUI()

        def initUI(self):
            self.configure(corner_radius=constants["width"] * 0.02, width=0, height=0)
            self.grid(padx=5, pady=5, sticky="nsew")

            self.product_name_label = ctk.CTkLabel(master=self, text=self.product_name, text_font=("Arial Black", 14), anchor="w", width=0)
            self.product_id_label = ctk.CTkLabel(master=self, text="#" + self.product_id, text_font=("Arial", 12), anchor="w", width=0)
            self.product_price_label = ctk.CTkLabel(master=self, text=self.product_price + "€", text_font=("Arial", 12), anchor="w", width=0)
            self.product_stock_label = ctk.CTkLabel(master=self, text="x" + self.product_stock, text_font=("Arial", 12), anchor="e", width=0)

            self.product_name_label.grid(row=0, column=0, pady=3, padx=10)
            self.product_id_label.grid(row=1, column=0, pady=3, padx=10)
            self.product_price_label.grid(row=2, column=0, pady=3, padx=10)
            self.product_stock_label.grid(row=1, column=1, pady=3, padx=10)
            