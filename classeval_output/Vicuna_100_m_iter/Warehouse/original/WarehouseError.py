
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







    def get_product_quantity(self, product_id):
        if product_id in self.inventory:
            return self.inventory[product_id]
        else:
            return False

    def create_order(self, order_id, product_id, quantity):
        if product_id in self.inventory and quantity > 0:
            self.orders[order_id] = {"product_id": product_id, "quantity": quantity, "status": "Shipped"}
            return True
        else:
            return False

    def change_order_status(self, order_id, status):
        orders = self.orders
        if order_id in orders:
            orders[order_id]["status"] = status
            return True
        else:
            return False

    def track_order(self, order_id):
        orders = self.orders
        if order_id in orders:
            status = orders[order_id]["status"]
            if status == "Shipped":
                return status
            elif status == "Not Shipped":
                return "Not Shipped"
            else:
                return "Unknown"
        else:
            return "Not Found"