class Product:
    def __init__(self, name, product_id, category, price, quantity):
        self.name = name
        self.product_id = product_id
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount):
        self.quantity += amount

    def is_available(self):
        return self.quantity > 0

    def total_price(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "name": self.name,
            "product_id": self.product_id,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity,
            "type": "Product"
        }

    def __str__(self):
        return (f"(Name of product: {self.name},"
                f" Id: {self.product_id}, "
                f"Category: {self.category}, "
                f"Price: {self.price}, "
                f"Quantity: {self.quantity})")
