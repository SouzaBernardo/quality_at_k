class Warehouse: 
    def __init__(self):
        """
        Initialize two fields.
        self.inventory is a dict that stores the products.
        self.inventory = {Product ID: Product}
        self.orders is a dict that stores the products in a order.
        self.orders = {Order ID: Order}
        """
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order


    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}
    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            print("Product ID not found in inventory.")
    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id, int
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        """
        if product_id in self.inventory:
            return self.inventory[product_id].quantity
        else:
            return False
    def create_order(self, order_id, product_id, quantity):
        # Check if product_id is in inventory
        if product_id not in self.inventory:
            return False
        # Check if the quantity is adequate
        if self.inventory[product_id]['quantity'] < quantity:
            return False
        # Create a new order
        order = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        # Add the new order to self.orders
        self.orders[order_id] = order
        # Update the quantity of the product in the inventory
        self.inventory[product_id]['quantity'] -= quantity
        return True
    def change_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False
    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        """
        if order_id in self.orders:
            return self.orders[order_id].status
        else:
            return False