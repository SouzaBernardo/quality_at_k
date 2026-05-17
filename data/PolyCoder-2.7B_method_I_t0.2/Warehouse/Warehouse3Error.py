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
        if product_id not in self.inventory:
            self.inventory[product_id] = {}
        if quantity not in self.inventory[product_id]:
            self.inventory[product_id][quantity] = {}
        self.inventory[product_id][quantity]['name'] = name
        self.inventory[product_id][quantity]['quantity'] = quantity
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['status'] = 'NEW'
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['created_by'] = self.name
        self.inventory[product_id][quantity]['updated_by'] = self.name
        self.inventory[product_id][quantity]['id'] = product_id
        self.inventory[product_id][quantity]['created_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity]['updated_at'] = datetime.datetime.now()
        self.inventory[product_id][quantity