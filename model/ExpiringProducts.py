from model.Product import Product

class ExpiringProducts(Product):
    def __init__(self, name, product_id, quantity, price, category, expiration_date):
        super().__init__(name, product_id, category, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self, today):
        return self.expiration_date < today

    def to_dict(self):
        data=super().to_dict()
        data["expiration_date"] = self.expiration_date
        data["type"] = "ExpiringProducts"
        return data

    def __str__(self):
        return (f"{super().info()},"
                f"Expiration date: {self.expiration_date},")