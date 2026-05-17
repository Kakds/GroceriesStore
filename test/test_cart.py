import unittest
from models.cart import Cart
from models.product import Product

class TestCart(unittest.TestCase):
    def test_add_item_to_cart(self):
        cart = Cart()
        apple = Product("1", "Apple", 1.5)

        cart.add_item(apple)

        self.assertTrue(len(cart.items) == 1)
        self.assertEqual(cart.items[0].name, "Apple")

    def test_cart_total(self):
        cart = Cart()
        cart.add_item(Product("1", "Apple", 1.5))
        cart.add_item(Product("2", "Bread", 2.0))
        cart.add_item(Product("3", "Milk", 3.5))

        self.assertEqual(cart.total(), 7.0)