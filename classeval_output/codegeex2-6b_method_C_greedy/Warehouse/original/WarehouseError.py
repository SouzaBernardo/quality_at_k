
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
        

        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
        else:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}



    def update_product_quantity(self, product_id, quantity):


    def update_product_quantity(self, product_id, quantity):
        

        self.inventory[product_id].quantity += quantity


    def get_product_quantity(self, product_id):


    def create_order(self, order_id, product_id, quantity):
        

        if product_id not in self.inventory:
            return False
        if quantity > self.inventory[product_id].quantity:
            return False
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        return True


    def change_order_status(self, order_id, status):


    def track_order(self, order_id):
        

        if order_id not in self.orders:
            return False
        else:
            return self.orders[order_id].status
