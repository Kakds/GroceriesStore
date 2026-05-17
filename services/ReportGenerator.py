class ReportGenerator:
    def generate_reports(self, products):
        report = "REPORT: \n"
        for p in products:
            report += (f"{p.name}, Quantity:{p.quantity}"
                       f"Value:{p.get_total_value():.2f}\n")
        return report

    def low_stock(self, products, threshold=5):
        low = [p for p in products if p.quantity <= threshold]
        report = "LOW_STOCK: \n"
        for p in low:
            report += f"({p.name}, Quantity:{p.quantity})\n"
        return report

    def summary(self, orders):
        total = sum(order.total_price for order in orders)

        return (
            "SALES SUMMARY: \n"
            f"Total Orders: {len(orders)}\n"
            f"Total Sum: {total:.2f}\n"
        )
