class Inventory_Manager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        new_list = []
        for p in self.products:
            if p.product_id != product_id:
                new_list.append(p)
        self.products = new_list

    def find_product(self, product_id):
        for p in self.products:
            if p.id == product_id:
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
            return ("No products found")

        result = ""
        for p in self.products:
            result += p.name + "\n"
        return result