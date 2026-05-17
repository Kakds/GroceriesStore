import unittest
from models.product import Product
from services.inventory_manager import InventoryManager

class TestInventory(unittest.TestCase):
    def test_add_product(self):
        manager = InventoryManager()
        manager.add_product(Product("10", "Bread", 1.0))
        self.assertTrue("10" in manager.products)

    def test_functional_filter(self):
        manager = InventoryManager()
        manager.add_product(Product("11", "Cheap", 5.0))
        manager.add_product(Product("12", "Expensive", 50.0))
        res = manager.get_expensive_products(10.0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].name, "Expensive")