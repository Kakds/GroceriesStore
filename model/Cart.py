class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                return
        self.items.append({"product": product, "quantity": quantity})

    def remove(self, product_id):
        self.items = [
            item for item in self.items
            if item["product"].product_id != product_id
        ]

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def display(self):
        if not self.items:
            return "No items found"
        result = "IN CART:\n"
        for item in self.items:
            p = item["product"]
            result += f"{p.name} x {item['quantity']} = {p.price * item['quantity']:.2f}\n"
        result += f"\nTOTAL PRICE: {self.calculate_total():.2f}"
        return result

    def clear(self):
        self.items = []
