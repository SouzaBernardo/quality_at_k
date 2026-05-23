
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
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        if product_id in self.inventory:
            if self.inventory[product_id]['quantity'] >= quantity:
                self.inventory[product_id]['quantity'] += quantity
            else:
                self.inventory[product_id]['quantity'] = quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}

    def update_product_quantity(self, product_id, quantity):
        product = self.get_product(product_id)
        if product:
            self.inventory[product_id] = product
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': product_id, 'quantity': quantity}

    def get_product_quantity(self, product_id):
        if product_id in self.inventory:
            return self.inventory[product_id]
        else:
            return False

    def create_order(self, order_id, product_id, quantity):
        if product_id in self.inventory and quantity <= self.inventory[product_id]:
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        else:
            return False

    def change_order_status(self, order_id, status):
        orders = self.orders
        if order_id in orders:
            orders[order_id]['status'] = status
            return False
        else:
            return None

    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        """
        if order_id in self.orders:
            return "Shipped"
        else:
            return False
