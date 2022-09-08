import tkinter as tk
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 

class Products:
    def __init__(self, root):
        label = tk.Label(root, text="Products")
        label.pack()

        apple = Product(root, "21353", "Apple", 1.3, 10)
        banana = Product(root, "21354", "Banana", 1.5, 20)
        orange = Product(root, "21355", "Orange", 1.7, 30)
        

        AddBtn(root, "Add new product", self.add)
        DeleteBtn(root, "Delete product", self.delete)

    def add(self):
        print("Add product")
    
    def delete(self):
        print("Delete product")

class Product:
    def __init__(self, root, product_id, product_name, product_price, product_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock

        self.initUI(root)

    def initUI(self, root):
        id = tk.Label(root, text=self.product_id)
        id.pack()

        name = tk.Label(root, text=self.product_name)
        name.pack()

        price = tk.Label(root, text=self.product_price)
        price.pack()

        stock = tk.Label(root, text=self.product_stock)
        stock.pack()