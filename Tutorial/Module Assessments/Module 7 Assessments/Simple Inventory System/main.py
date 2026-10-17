class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"{self.name} | Price: ${self.price:.2f} | Quantity: {self.quantity}")

    def update_quantity(self, amount):
        if self.quantity + amount < 0:
            print(f"Not enough stock of '{self.name}'. Only {self.quantity} available.")
            return False
        self.quantity += amount
        if amount < 0:
            print(f"Sold {-amount} of '{self.name}'. Remaining: {self.quantity}")
        else:
            print(f"Restocked {amount} of '{self.name}'. Now in stock: {self.quantity}")
        return True

    def total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added product: {product.name}")

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def sell(self, name, amount):
        product = self.find_product(name)
        if product is None:
            print(f"'{name}' is not in the inventory.")
            return False
        return product.update_quantity(-amount)

    def restock(self, name, amount):
        product = self.find_product(name)
        if product is None:
            print(f"'{name}' is not in the inventory.")
            return False
        return product.update_quantity(amount)

    def display_all(self):
        if len(self.products) == 0:
            print("The inventory is empty.")
            return
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        return sum(product.total_value() for product in self.products)


def main():
    inventory = Inventory()

    print("--- Adding products ---")
    inventory.add_product(Product("Notebook", 2.50, 100))
    inventory.add_product(Product("Pen", 0.75, 250))
    inventory.add_product(Product("Backpack", 25.00, 20))

    print("\n--- Inventory ---")
    inventory.display_all()
    print(f"Total inventory value: ${inventory.total_inventory_value():.2f}")

    print("\n--- Adding a new product ---")
    inventory.add_product(Product("Calculator", 12.99, 15))

    print("\n--- Selling 30 notebooks ---")
    inventory.sell("Notebook", 30)

    print("\n--- Selling 50 backpacks (more than in stock) ---")
    inventory.sell("Backpack", 50)

    print("\n--- Restocking 40 pens ---")
    inventory.restock("Pen", 40)

    print("\n--- Final inventory ---")
    inventory.display_all()
    print(f"Total inventory value: ${inventory.total_inventory_value():.2f}")

main()