import customtkinter as ctk
from constants import constants
from components.addBtn import AddBtn
from components.deleteBtn import DeleteBtn  
import json
import random
from datetime import date

class Orders(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loadProducts()
        self.loadOrders()

        self.initUI()  

    def initUI(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.orders_list_frame = ctk.CTkFrame(master=self)
        self.orders_list_frame.configure(corner_radius=0)
        self.orders_list_frame.grid(row=0, column=0, sticky="nsew")

        self.orders_list_frame_title = ctk.CTkLabel(master=self.orders_list_frame, text="Orders activity",  width=120, height=25, text_font=("Arial Black", 12), anchor="nw")
        self.orders_list_frame_title.grid(row=0, column=0,  pady=10, padx=10, sticky="nsew")

        self.configure_frame = ctk.CTkFrame(master=self)
        self.configure_frame.configure(corner_radius=0)
        self.configure_frame.grid(row=1, column=0, sticky="nsew")

        self.createBtn = AddBtn(text="Create new order", command_name=self.createOrder, master=self.configure_frame)
        self.cancelBtn = DeleteBtn(text="Cancel order", command_name=self.cancelOrder, master=self.configure_frame)
        self.createBtn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.cancelBtn.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        self.orders_list = []
        i = 0
        self.orders = self.orders_available_from_file["orders"]
        for order in self.orders:
            if i == 9:
                break
            for key, value in order.items():
                self.orders_list.append(self.Order(self.orders_list_frame, order_customer=value["order_customer"], order_product=value["order_product"], order_product_price=value["order_price_per_unit"], order_quantity=value["order_quantity"], order_id=key, order_status=value["order_status"], order_date=value["order_date"]))
                self.orders_list[i].grid(column=0, row=i + 1, pady=10, padx=10, sticky="nsew")

                i += 1

    def loadOrders(self):
        with open('./src/orders.json') as json_orders:
            try :
                data = json.load(json_orders)
            except:
                print("Error loading products")
                return

        self.orders_available_from_file = data
        self.orders = self.orders_available_from_file["orders"]

    def loadProducts(self):
        with open('./src/products.json') as json_products:
            try :
                data = json.load(json_products)
            except:
                print("Error loading products")
                return

        self.products_available_from_file = data
        self.products_available = self.products_available_from_file["products_available"]

    def createOrder(self):
        self.create_window = ctk.CTkToplevel()
        self.create_window.title("Create a new order")
        self.create_window.geometry("400x400")

        products_names = []
        for product in self.products_available:
            for key, value in product.items():
                products_names.append(value["product_name"])
        
        self.combobox = ctk.CTkOptionMenu(master=self.create_window, values=products_names)  
        self.combobox.grid(row=0, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        # Select quantity
        self.quantity = ctk.CTkComboBox(master=self.create_window, values=[str(i) for i in range(1, 100)])
        self.quantity.grid(row=1, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        self.customer_name_entry = ctk.CTkEntry(master=self.create_window, placeholder_text="Customer name", width=120, height=25, border_width=2, corner_radius=10)
        self.customer_name_entry.grid(row=2, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        confirmBtn = AddBtn(text="Confirm", command_name=self.confirm, master=self.create_window)
        cancelBtn = DeleteBtn(text="Cancel", command_name=self.cancel, master=self.create_window)

        confirmBtn.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
        cancelBtn.grid(row=3, column=1, pady=10, padx=10, sticky="nsew")

    def confirm(self):
        choice = self.combobox.get()
        for product in self.products_available:
            for key, value in product.items():
                if value["product_name"] == choice:
                    product_choice = product 

        for key, value in product_choice.items():
            product_price = value["product_price"]
            product_name = value["product_name"]
            product_stock = value["product_stock"]

        
        if int(product_stock) < int(self.quantity.get()):
            self.quantity.configure(fg_color="red")
            return

        order_id = "".join([random.choice("0123456789") for n in range(5)])

        today = date.today()

        new_order = {
            order_id: {
                "order_product": str(product_name),
                "order_price_per_unit": str(product_price),
                "order_quantity": str(self.quantity.get()),
                "order_customer": str(self.customer_name_entry.get()),
                "order_date": str(today.strftime("%d/%m/%Y")),
                "order_status": "Pending"
            }
        }


        self.orders_available_from_file["orders"].append(new_order)
        with open("./src/orders.json", "w") as orders_file:
            json.dump(self.orders_available_from_file, orders_file, indent=4)

        self.loadProducts()
        self.loadOrders()
        self.initUI()

        self.create_window.destroy()

    def cancel(self):
        self.create_window.destroy()

    def cancelOrder(self):
        self.delete_window = ctk.CTkToplevel()
        self.delete_window.title("Delete a order")
        self.delete_window.geometry("400x400")

        orders_customer = []
        for order in self.orders:
            for key, value in order.items():
                orders_customer.append(value["order_customer"])
        
        self.cancelMenu = ctk.CTkOptionMenu(master=self.delete_window, values=orders_customer)  
        self.cancelMenu.grid(row=0, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

        deleteBtn = AddBtn(text="Delete selection", command_name=self.deleteConfirm, master=self.delete_window)
        cancelBtn = DeleteBtn(text="Cancel", command_name=self.deleteCancel, master=self.delete_window)

        deleteBtn.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
        cancelBtn.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")

    def deleteConfirm(self):
        choice = self.cancelMenu.get()

        for order in self.orders:
            for key, value in order.items():
                if value["order_customer"] == choice:
                    self.orders.remove(order)
        
        with open("./src/orders.json", "w") as orders_file:
            json.dump(self.orders_available_from_file, orders_file, indent=4)

        self.loadProducts()
        self.loadOrders()
        self.initUI()

        self.delete_window.destroy()

    def deleteCancel(self):
        self.delete_window.destroy()

    class Order(ctk.CTkFrame):
        def __init__(self, *args, order_customer, order_product, order_product_price, order_quantity, order_id, order_status, order_date, **kwargs):
            super().__init__(*args, **kwargs)

            self.order_customer = str(order_customer)
            self.order_product = str(order_product)
            self.order_quantity = str(order_quantity)
            self.order_id = str(order_id)
            self.order_status = str(order_status)
            self.order_cost = str(float(order_quantity) * float(order_product_price))
            self.order_date = str(order_date)

            self.initUI()

        def changeStatus(self, event):
            print("Button pressed")
            dialog = ctk.CTkInputDialog(master=None, text="Type in a number:", title="Test")

        def initUI(self):
            self.configure(corner_radius=constants["width"] * 0.02, height=0)
            self.grid(padx=5, pady=5, sticky="nsew")

            self.order_product_label = ctk.CTkLabel(master=self, text=self.order_product, text_font=("Arial Black", 14), anchor="w", width=0)
            self.order_product_quantity_label = ctk.CTkLabel(master=self, text="x" + self.order_quantity, text_font=("Arial", 12), anchor="w", width=0)
            self.order_customer_label_label = ctk.CTkLabel(master=self, text=self.order_customer, text_font=("Arial", 12), anchor="w", width=0)
            self.order_cost_label = ctk.CTkLabel(master=self, text=self.order_cost + "€", text_font=("Arial", 12), anchor="w", width=0)
            self.order_date_label = ctk.CTkLabel(master=self, text=self.order_date, text_font=("Arial", 12), anchor="w", width=0)

            #optionmenu_var = ctk.StringVar(value=self.order_status)
            #self.order_product_status_label = ctk.CTkOptionMenu(master=self, values=["Pending", "In progress", "Done"], variable=optionmenu_var, width=0, text_font=("Arial", 12))
            if self.order_status == "Pending":
                self.order_product_status_label = ctk.CTkLabel(master=self, text=self.order_status, text_font=("Arial", 12), text_color="orange", anchor="w", width=0)
            elif self.order_status == "Completed":
                self.order_product_status_label = ctk.CTkLabel(master=self, text=self.order_status, text_font=("Arial", 12), text_color="green", anchor="w", width=0)
            elif self.order_status == "Cancelled":
                self.order_product_status_label = ctk.CTkLabel(master=self, text=self.order_status, text_font=("Arial", 12), text_color="red", anchor="w", width=0)

            self.order_product_label.grid(row=0, column=0, sticky="nsew", padx=10)
            self.order_product_quantity_label.grid(row=0, column=1, sticky="nsew", padx=10)
            self.order_product_status_label.grid(row=0, column=2, sticky="nsew", padx=10)
            self.order_customer_label_label.grid(row=1, column=0, sticky="nsew", padx=10)
            self.order_cost_label.grid(row=1, column=1, sticky="nsew", padx=10)
            self.order_date_label.grid(row=1, column=2, sticky="nsew", padx=10)
