import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn  

class Orders(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()
        return

        order1 = Order(root, "01/12/2022", "25314", "Nathan_Brodin", "CANCELLED", 1.4)

        AddBtn(root, "Create new order", self.add)
        DeleteBtn(root, "Cancel order", self.delete)

    def initUI(self):
        return

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
        return