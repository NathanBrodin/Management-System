import tkinter as tk
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 

class Products:
    def __init__(self, root):
        label = tk.Label(root, text="Products")
        label.pack()

        AddBtn(root, "Add new product", self.add)
        DeleteBtn(root, "Delete product", self.delete)

    def add(self):
        print("Add product")
    
    def delete(self):
        print("Delete product")

class Product:
    def __init__(self, product_id, product_name, product_price, product_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock