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
        Add product to inventory and increase the quantity if it already exists in the inventory.
        Otherwise, add a new product to the inventory.
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
    

    def get_product_quantity(self, product_id):
        """
        Get the quantity of a specific product by product_id.
        :param product_id: int
        :return: if the product_id is in inventory then return the corresponding quantity,
                 or False otherwise.
        """
        if product_id in self.inventory:
            return self.inventory[product_id].quantity
        else:
            return False
    

    def create_order(self, order_id, product_id, quantity):
        """
        Create a order which includes the information of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of product that be selected.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        """
        if product_id not in self.inventory:
            return False
        if self.inventory[product_id]['quantity'] < quantity:
            return False
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
    

    def change_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False
    

    def track_order(self, order_id):
        """
        Get the status of a specific order.
        :param order_id: int
        :return: str or False if the order_id is not in self.orders
        """
        if order_id in self.orders:
            return self.orders[order_id].status
        else:
            return False