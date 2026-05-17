import datetime

class Order:
    def __init__(self, order_id, cart ):
        self.order_id = order_id
        self.cart = cart
        self.date_now = datetime.datetime.now()
        self.total_price = cart.calculate_total_price()

    def order_receipt(self):
        receipt=f"\n ORDER RECEIPT\n"
        receipt += f"Order ID: {self.order_id}\n"
        receipt += f"Order Date: {self.date_now}\n"

        for item in self.cart.items:
            p = item["product"]
            quantity = item["quantity"]
            receipt += f"{p.name} x {quantity} = {p.price * quantity:.2f}\n"

        receipt += f"TOTAL: {self.total_price:.2f}\n"

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "date_now": self.date_now,
            "total_price": self.total_price,
        }
