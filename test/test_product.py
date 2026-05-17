import unittest
from models.product import Product
from models.expiring_product import ExpiringProduct

class TestProduct(unittest.TestCase):
    def test_product_encapsulation(self):
        p = Product("1", "Apple", 1.5, 10, "Fruits")
        self.assertEqual(p.name, "Apple")
        self.assertEqual(p.price, 1.5)
        self.assertEqual(p.quantity, 10)
    def test_inheritance(self):
        pp = PerishableProduct(
            "2", "Milk", 2.0, 10, "Dairy", "2026-12-01"
        )
        self.assertEqual(pp.name, "Milk")
        self.assertEqual(pp.expiry_date, "2026-12-01")

    def test_polymorphism_str(self):
        pp = ExpiringProduct(
            "3", "Yogurt", 3.0, 5, "Dairy", "2026-10-01"
        )
        result = str(pp)
        self.assertIn("Yogurt", result)
        self.assertIn("2026", result)

if __name__ == "__main__":
    unittest.main()
