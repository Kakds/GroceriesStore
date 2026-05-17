class Cart(object):
    def __init__(self,items):
        self.items = []

    def append(self,product, quantity):
        for item in self.items:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                break

        self.items.append({"product":product,"quantity":quantity})

    def remove(self,product_id):
        new_items= []
        for item in self.items:
            if item["product"].product_id != product_id:
                new_items.append(item)
        self.items= new_items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]

    def display(self):
        if not self.items:
            return "No items found"
        result = "IN CART: \n"
        for item in self.items:
            p = item["product"]
            result += f"{p.name} x {item["quantity"]} = {p.price}*{item["quantity"]:.2f}\n"
        result += f"\nTOTAL PRICE: {self.calculate_total():.2f}"
        return result

    def clear(self):
        self.items = []