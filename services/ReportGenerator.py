class ReportGenerator:
    def generate_reports(self, products):
        report = "PRODUCT REPORT:\n"
        for p in products:
            value = p.price * p.quantity
            report += (
                f"{p.name}, Quantity: {p.quantity}, "
                f"Value: {value:.2f}\n"
            )
        return report

    def low_stock(self, products, threshold=5):
        low = [p for p in products if p.quantity <= threshold]
        report = "LOW STOCK REPORT:\n"
        if not low:
            return report + "No low stock items.\n"
        for p in low:
            report += f"{p.name}, Quantity: {p.quantity}\n"
        return report

    def summary(self, orders):
        total = 0
        for o in orders:
            total += o["total_price"]
        return (
            "SALES SUMMARY:\n"
            f"Total Orders: {len(orders)}\n"
            f"Total Revenue: {total:.2f}\n"
        )
