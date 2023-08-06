class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_cost = 0
    def add_item(self,items):
        self.items.append(items)
        self.total_cost += items.price
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            self.total_cost -= item.price
    def empty_cart(self):
        self.items = []
        self.total_cost = 0
        print("Cart is empty")
    def print_cart_info(self):
        for item in self.items:
            print(f"{item.name} ${self.total_cost}")

class Item:
    def __init__(self,name,price):
            self.name = name
            self.price = price
cart = ShoppingCart()
toilet_paper = Item("Toilet Paper",2)
shampoo = Item("Shampoo",3)
spectacles = Item("Spectacles",40)

cart.empty_cart()
cart.print_cart_info()
cart.add_item(shampoo)
cart.print_cart_info()
cart.remove_item(shampoo)
cart.print_cart_info()


