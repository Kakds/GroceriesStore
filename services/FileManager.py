import json
from models.product import Product
from models.expiring_product import ExpiringProducts

class FileManager:
    def save_products(self, products, file_name):
        data = [p.to_dict() for p in products]
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_products(self, file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
            products = []
            for p in data:
                if p.get("type") == "ExpiringProducts":
                    products.append(
                        ExpiringProducts(
                            p["product_id"],
                            p["name"],
                            p["price"],
                            p["quantity"],
                            p["category"],
                            p.get("expiration_date")
                        )
                    )
                else:
                    products.append(
                        Product(
                            p["product_id"],
                            p["name"],
                            p["price"],
                            p["quantity"],
                            p["category"]
                        )
                    )
            return products
        except FileNotFoundError:
            return []

    def save_orders(self, orders, file_name):
        data = [o.to_dict() for o in orders]
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_orders(self, file_name):
        try:
            with open(file_name, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
