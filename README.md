Grocery Store Management System
Our team: Arysbek Kaisar and Uazhanov Sultan from SE-2511

The final project for the course Introduction to Programming 2.
This is a fully modular CLI console system for managing a grocery store and inventory. The project simulates the basic operation of a store: viewing a catalog, managing a shopping cart, and placing an order, saving all data to files

Architecture and module overview

The project is built on a clean architecture with a clear separation of data models, business logic, auxiliary utilities and tests

 Data models - Basic OOP
Product: The base class of the product. Stores basic data: encapsulated ID, name, and price.
PerishableProduct: Inherits from Product. Adds an expiration date and redefines the information output method (Polymorphism).
Customer: Stores the buyer's data and automatically verifies the correctness of the email when creating it.
Cart: Shopping cart. Manages the selected items (using dictionaries and arrays) and calculates the total amount.
Order: The order. Combines the Customer and Cart objects (Association) and generates a unique receipt number

Business Logic Services — Logic and Data
InventoryManager: Manages the store's catalog. Uses functional programming tools (map, filter, lambda) to apply discounts or filter products by price.
FileManager: Responsible for saving data. Downloads the initial product catalog from JSON and adds data about successful sales to a CSV file.
ReportGenerator: Calculates the total revenue. Passes data through a custom generator to simulate efficient work with large amounts of data

Utilities (utils) — Auxiliary tools
decorators.py : Contains the @log_action decorator, which is used to track and output information about called functions to the console.
'validators.py : Responsible for validating input using regular regex expressions, for example, to verify the email format.
generators.py `: Contains custom iterators/generators for step-by-step list processing

Tests — QA Quality Control
It contains detailed unit tests written on the built-in unittest module. They check the principles of OOP (encapsulation/polymorphism), the mathematics of the bucket, the functional tools of the inventory, and the correctness of file input/output
