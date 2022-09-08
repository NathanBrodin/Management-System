import tkinter as tk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn  

class Orders:
    def __init__(self, root):
        orders_frame = tk.Frame(root, bg="red", width=constants["width"]*0.3, height=constants["height"]*0.98)
        orders_frame.pack( side = tk.RIGHT )
        return

        label = tk.Label(root, text="Orders")
        label.pack()

        order1 = Order(root, "01/12/2022", "25314", "Nathan_Brodin", "CANCELLED", 1.4)

        AddBtn(root, "Create new order", self.add)
        DeleteBtn(root, "Cancel order", self.delete)

    def add(self):
        print("Add order")

    def delete(self):
        print("Delete order")

class Order:
    def __init__(self, root, order_date, order_id, order_customer, order_status, order_cost):
        self.order_date = order_date
        self.order_id = order_id
        self.order_customer = order_customer
        self.order_status = order_status
        self.order_cost = order_cost

        self.initUI(root)

    def initUI(self, root):
        date = tk.Label(root, text=self.order_date)
        date.pack()

        id = tk.Label(root, text=self.order_id)
        id.pack()

        customer = tk.Label(root, text=self.order_customer)
        customer.pack()

        status = tk.Label(root, text=self.order_status)
        status.pack()

        cost = tk.Label(root, text=self.order_cost)
        cost.pack()