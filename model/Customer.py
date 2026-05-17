class Customer:
    def __init__(self, name, customer_id, phone):
        self.name = name
        self.customer_id = customer_id
        self.phone = phone
        self.cart = None

    def add_cart(self, cart):
        self.cart = cart

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Customer ID: {self.customer_id}\n"
            f"Phone: {self.phone}"
        )
