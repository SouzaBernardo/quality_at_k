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





    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        If the resulting quantity is negative, set the quantity to zero.
        """
        if product_id in self.inventory:
            product = self.inventory[product_id]
            product['quantity'] += quantity
            if product['quantity'] < 0:
                product['quantity'] = 0
        else:
            raise ValueError("Product ID not found in inventory.")



    def create_order(self, order_id, product_id, quantity):
        """
        Create a order which includes the infomation of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Pending'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of product that be selected.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        """
        if product_id in self.inventory:
            product = self.inventory[product_id]
            if product['quantity'] >= quantity:
                order = {'product_id': product_id, 'quantity': quantity,'status': 'Pending'}
                self.orders[order_id] = order
                return True
            else:
                return False
        else:
            return False



    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        """
        if order_id in self.orders:
            order = self.orders[order_id]
            if order['status'] == 'Shipped':
                return 'Shipped'
            else:
                return 'Pending'
        else:
            return False