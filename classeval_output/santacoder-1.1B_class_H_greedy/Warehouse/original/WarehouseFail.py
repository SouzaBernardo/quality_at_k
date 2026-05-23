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
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 3}}
        """

    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id, int
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.get_product_quantity(1)
        3
        >>> warehouse.get_product_quantity(2)
        False
        """

    def create_order(self, order_id, product_id, quantity):
        """
        Create a order which includes the infomation of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of product that be selected.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2,'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return False: only if the order_id is not in self.orders
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.change_order_status(1, "done")
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2,'status': 'done'}}
        """

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

    def get_all_orders(self):
        """
        Get all orders in self.orders.
        :return: self.orders
        """

    def get_all_products(self):
        """
        Get all products in self.inventory.
        :return: self.inventory
        """

    def get_all_orders_with_status(self):
        """
        Get all orders in self.orders with status.
        :return: self.orders
        """

    def get_all_products_with_status(self):
        """
        Get all products in self.inventory with status.
        :return: self.inventory
        """


class Product:
    """
    The class manages the product information.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize two fields.
        self.name is the product name.
        self.price is the product price.
        self.quantity is the product quantity.
        >>> product = Product("product1", 100, 3)
        >>> product.name
        'product1'
        >>> product.price
        100
        >>> product.quantity
        3
        """

    def get_name(self):
        """
        Get the product name.
        :return: self.name
        """

    def get_price(self):
        """
        Get the product price.
        :return: self.price
        """

    def get_quantity(self):
        """
        Get the product quantity.
        :return: self.quantity
        """


class Order:
    """
    The class manages the order information.
    """

    def __init__(self, product_id, quantity, status):
        """
        Initialize two fields.
        self.product_id is the product id.
        self.quantity is the product quantity.
        self.status is the order status.
        >>> order = Order(1, 2, "Shipped")
        >>> order.product_id
        1
        >>> order.quantity
        2
        >>> order.status
        'Shipped'
        """

    def get_product_id(self):
        """
        Get the product id.
        :return: self.product_id
        """

    def get_quantity(self):
        """
        Get the product quantity.
        :return: self.quantity
        """

    def get_status(self):
        """
        Get the order status.
        :return: self.status
        """


class WarehouseTest(unittest.TestCase):
    """
    The class manages the test cases.
    """

    def test_add_product(self):
        """
        Test add_product method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 3}}
        """

    def test_update_product_quantity(self):
        """
        Test update_product_quantity method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """

    def test_get_product_quantity(self):
        """
        Test get_product_quantity method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.get_product_quantity(1)
        3
        >>> warehouse.get_product_quantity(2)
        False
        """

    def test_create_order(self):
        """
        Test create_order method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2,'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """

    def test_change_order_status(self):
        """
        Test change_order_status method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.change_order_status(1, "done")
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2,'status': 'done'}}
        """

    def test_track_order(self):
        """
        Test track_order method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        >>> warehouse.track_order(2)
        False
        """

    def test_get_all_orders(self):
        """
        Test get_all_orders method.
        >>> warehouse = Warehouse()
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.get_all_orders()
        {1: {'product_id': 1, 'quantity': 2,'status': 'Shipped'}}