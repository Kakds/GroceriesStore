import unittest
from model.Cart import Cart
from model.Croduct import Product

class TestCart(unittest.TestCase):
    def test_add_item_to_cart(self):
        cart = Cart()
        apple = Product("1", "Apple", 1.5, 10, "Fruits")
        cart.add_item(apple, 1)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"].name, "Apple")

    def test_cart_total(self):
        cart = Cart()
        cart.add_item(Product("1", "Apple", 1.5, 10, "Fruits"), 1)
        cart.add_item(Product("2", "Bread", 2.0, 10, "Bakery"), 1)
        cart.add_item(Product("3", "Milk", 3.5, 10, "Dairy"), 1)
        self.assertEqual(cart.calculate_total(), 7.0)

if __name__ == "__main__":
    unittest.main()
