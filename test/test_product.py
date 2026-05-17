import unittest
from models.product import Product
from models.perishable_product import PerishableProduct

class TestProduct(unittest.TestCase):
    def test_product_encapsulation(self):
        p = Product("1", "Apple", 1.5)
        self.assertEqual(p.name, "Apple")

    def test_polymorphism(self):
        pp = PerishableProduct("2", "Milk", 2.0, "2024-01-01")
        self.assertTrue("Expires" in pp.display_info())