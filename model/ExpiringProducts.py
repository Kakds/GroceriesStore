from model.product import Product


class ExpiringProducts(Product):
    def __init__(self, product_id, name, price, quantity, category, expiration_date):
        super().__init__(product_id, name, price, quantity, category)
        self.expiration_date = expiration_date

    def is_expired(self, today):
        return self.expiration_date < today

    def to_dict(self):
        data = super().to_dict()
        data["expiration_date"] = self.expiration_date
        data["type"] = "ExpiringProducts"
        return data

    def __str__(self):
        return (
            super().__str__() +
            f"\nExpiration date: {self.expiration_date}"
        )
