class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [
            p for p in self.products
            if p.product_id != product_id
        ]

    def find_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None

    def update_product(self, product_id, amount):
        product = self.find_product(product_id)
        if product:
            product.quantity += amount
            return True
        return False

    def list_products(self):
        if not self.products:
            return "No products found"
        result = ""
        for p in self.products:
            result += (
                f"ID: {p.product_id}, "
                f"Name: {p.name}, "
                f"Price: {p.price}, "
                f"Qty: {p.quantity}, "
                f"Category: {p.category}\n"
            )
        return result
