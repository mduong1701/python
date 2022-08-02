class Store:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products
    
    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        sold = self.products.pop(id)
        sold.print_info()

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
        
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
    def show_inventory(self):
        for i in range(len(self.products)):
            self.products[i].print_info()

class Product:
    def __init__(self, p_name, price, category):
        self.p_name = p_name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + (percent_change / 100)
        else:
            self.price *= 1 - (percent_change / 100)
        
    def print_info(self):
        print("Name: ", self.p_name, 
            "\nCategory: ", self.category,
            "\nPrice: $", self.price)
    
my_store = Store("Mango")
my_store.add_product(Product("shirt", 100, "top"))
my_store.add_product(Product("t-shirt", 10, "top"))
my_store.add_product(Product("jeans", 200, "bottom"))
my_store.add_product(Product("shorts", 80, "bottom"))
my_store.add_product(Product("pants", 150, "bottom"))
my_store.show_inventory()
print("--------------------------------------------------------")
my_store.inflation(10)
my_store.show_inventory()
print("--------------------------------------------------------")
my_store.set_clearance( "bottom",50)
my_store.show_inventory()
print("--------------------------------------------------------")
my_store.sell_product(4)
print("--------------------------------------------------------")
my_store.show_inventory()