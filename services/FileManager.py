import json


class FileManager:
    def save_products(self, products, file_name):
        data = [p.to_dict() for p in products]

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def load_products(self, file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_orders(self, orders, file_name):
        data = [o.to_dict() for o in orders]
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)