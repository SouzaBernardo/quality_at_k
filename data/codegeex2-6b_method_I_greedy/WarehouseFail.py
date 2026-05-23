class Warehouse:  
    """
    The class manages inventory and orders, including adding products, updating product quantities, retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

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
        
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}


    def update_product_quantity(self, product_id, quantity):


    def update_product_quantity(self, product_id, quantity):
        

    def get_product_quantity(self, product_id):


    def get_product_quantity(self, product_id):
        

    def create_order(self, order_id, product_id, quantity):


    def change_order_status(self, order_id, status):


    def get_order_status(self, order_id):


    def get_order_status(self, order_id):





    def change_order_status(self, order_id, status):


    def track_order(self, order_id):