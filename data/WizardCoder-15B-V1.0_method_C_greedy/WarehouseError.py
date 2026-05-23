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
        """
        Create a order which includes the infomation of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of product that be selected.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        """
        if product_id not in self.inventory:
            return False
        if quantity > self.inventory[product_id].quantity:
            return False
        order = {'product_id': product_id, 'quantity': quantity,'status': 'Shipped'}
        self.orders[order_id] = order
        return True

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return False: only if the order_id is not in self.orders
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
            return True
        else:
            return False