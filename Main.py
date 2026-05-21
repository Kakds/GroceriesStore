from model.Product import Product
from model.ExpiringProducts import ExpiringProducts
from model.Cart import Cart
from model.Order import Order
from services.Inventory_Manager import InventoryManager
from services.ReportGenerator import ReportGenerator
from services.FileManager import FileManager

def main():
    inventory = InventoryManager()
    file_manager = FileManager()
    report = ReportGenerator()
    products = file_manager.load_products("data/products.json")
    for p in products:
        inventory.add_product(p)
    cart = Cart()
    while True:
        print("\n| GROCERY STORE SYSTEM |")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            print(inventory.list_products())

        elif choice == "2":
            product_id = input("Enter product ID: ")
            product = inventory.find_product(product_id)
            if product:
                qty = int(input("Enter quantity: "))
                cart.add_item(product, qty)
                print("Added to cart!")
            else:
                print("Product not found!")

        elif choice == "3":
            print(cart.display())

        elif choice == "4":
            order_id = input("Enter order ID: ")
            order = Order(order_id, cart)
            print(order.order_receipt())
            file_manager.save_orders([order], "data/sales.json")
            cart.clear()
            print("Order completed!")

        elif choice == "5":
            print(report.generate_reports(inventory.products))
            print(report.low_stock(inventory.products))
            orders_data = file_manager.load_orders("data/sales.json")
            print(report.summary(orders_data))

        elif choice == "6":
            print("Thank you for your purchase!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
