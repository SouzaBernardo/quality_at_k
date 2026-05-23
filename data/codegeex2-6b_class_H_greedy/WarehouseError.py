class Product:
    """
    The class manages products.
    """

    def __init__(self, product_id, name, quantity):
        """
        Initialize three fields.
        self.product_id is the id of product.
        self.name is the name of product.
        self.quantity is the quantity of product.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        """
        Return the string representation of product.
        :return: str, the string representation of product.
        """
        return f"{self.product_id}: {self.name}, {self.quantity}"


class Order:
    """
    The class manages orders.
    """

    def __init__(self, order_id, product_id, quantity, status):
        """
        Initialize four fields.
        self.order_id is the id of order.
        self.product_id is the id of product.
        self.quantity is the quantity of product.
        self.status is the status of order.
        :param order_id: int
        :param product_id: int
        :param quantity: int, the quantity of product that be selected.
        :param status: str, the state that is going to change to
        """
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.status = status

    def __str__(self):
        """
        Return the string representation of order.
        :return: str, the string representation of order.
        """
        return f"{self.order_id}: {self.product_id}, {self.quantity}, {self.status}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()