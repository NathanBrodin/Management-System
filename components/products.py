import tkinter as tk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 
import json

class Products:
    def __init__(self, root):
        products_frame = tk.Frame(root, bg="green", width=constants["width"]*0.7, height=constants["height"]*0.98)
        products_frame.pack( side = tk.LEFT )

        label = tk.Label(products_frame, text="Products")
        label.pack( side=tk.TOP )

        self.products_available = []
        self.loadProducts()

        apple = Product(root, "21353", "Apple", 1.3, 10)
        banana = Product(root, "21354", "Banana", 1.5, 20)
        orange = Product(root, "21355", "Orange", 1.7, 30)
        
        self.add("00001", "Pineapple", 2.3, 40)
        self.add("00002", "Banana", 1.5, 20)
        self.add("00003", "Orange", 1.7, 30)
        self.add("00004", "Apple", 1.3, 10)

        AddBtn(root, "Add new product", self.addProduct("21356", "Pineapple", 2.3, 40))
        DeleteBtn(root, "Delete product", self.delete)

    def addProduct(self, product_id, product_name, product_price, product_stock):
        new_product = {
            product_id : {
                "product_name": product_name,
                "product_price": product_price,
                "product_stock": product_stock
            }
        }

        with open("./src/products.json", "a") as products_file:
            json.dump(new_product, products_file, indent=4)

        print("New product added")
    
    def deleteProduct(self):
        print("Product deleted")

    def loadProducts(self):
        with open('./src/products.json') as json_products:
            try :
                data = json.load(json_products)
                print(data)
            except:
                print("Error loading products")
        

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