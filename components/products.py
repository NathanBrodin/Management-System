import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn 
import json

class Products(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return
    
        self.loadProducts()
        self.initUI()

        return
        apple = Product(root, "21353", "Apple", 1.3, 10)
        banana = Product(root, "21354", "Banana", 1.5, 20)
        orange = Product(root, "21355", "Orange", 1.7, 30)

        AddBtn(root, "Add new product", self.addProduct("21356", "Pineapple", 2.3, 40))
        DeleteBtn(root, "Delete product", self.deleteProduct)

    def initUI(self):
        return

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
        

class Product:
    def __init__(self, root, product_id, product_name, product_price, product_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock

        self.initUI(root)

    def initUI(self, root):
        return