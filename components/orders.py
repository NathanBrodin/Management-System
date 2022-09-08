import tkinter as tk
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn  

class Orders:
    def __init__(self, root):
        label = tk.Label(root, text="Orders")
        label.pack()

        AddBtn(root, "Create new order", self.add)
        DeleteBtn(root, "Cancel order", self.delete)

    def add(self):
        print("Add order")

    def delete(self):
        print("Delete order")

class Order:
    def __init__(self, order_date, order_id, order_customer, order_status, order_cost):
        self.order_date = order_date
        self.order_id = order_id
        self.order_customer = order_customer
        self.order_status = order_status
        self.order_cost = order_cost