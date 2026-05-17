import unittest
from model.Product import Product
from services.Inventory_Manager import InventoryManager

class TestInventory(unittest.TestCase):
    def test_add_product(self):
        manager = InventoryManager()
        product = Product("10", "Bread", 1.0, 10, "Bakery")
        manager.add_product(product)
        self.assertTrue(
            any(p.product_id == "10" for p in manager.products)
        )

    def test_find_product(self):
        manager = InventoryManager()
        product = Product("11", "Milk", 2.5, 10, "Dairy")
        manager.add_product(product)
        found = manager.find_product("11")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Milk")

if __name__ == "__main__":
    unittest.main()
