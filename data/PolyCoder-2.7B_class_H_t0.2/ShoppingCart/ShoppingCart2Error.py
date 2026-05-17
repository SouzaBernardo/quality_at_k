class ShoppingCart:
    """
    The class manages items, their prices, quantities, and allows to for add, removie, view items, and calculate the total price.
    """

    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """
        self.items = {}


    def add_item(self, item, price, quantity=1):
        """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity:int, The number of items, defaults to 1
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        self.items = {"apple":{"price":1, "quantity":5}}
        """


    def remove_item(self, item, quantity=1):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item:string, Item to be subtracted in quantity
        :param quantity:int, Quantity to be subtracted
        :return:None
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        self.items = {"apple":{"price":1, "quantity":2}}
        """


    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":2}}
        """


    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        """


    def quantities(self) -> dict:
        """
        Return the current shopping list quantities
        :return:dict, the current shopping list quantities
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.quantities()
        {"apple":{"price":1, "quantity":5}, "banana":{"price":2, "quantity":3}}
        """


    def add_item_quantity(self, item, quantity):
        """
        Add the specified quantity of item to the shopping list items
        :param item:string, Item to be added
        :param quantity:int, Quantity to be added
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item_quantity("apple", 1, 5)
        self.items = {"apple":{"price":1, "quantity":5}}
        """


    def remove_item_quantity(self, item, quantity):
        """
        Subtract the specified quantity of item from the shopping list items
        :param item:string, Item to be subtracted in quantity
        :param quantity:int, Quantity to be subtracted
        :return:None
        >>> shoppingcart.add_item_quantity("apple", 1, 5)
        >>> shoppingcart.remove_item_quantity("apple", 3)
        self.items = {"apple":{"price":1, "quantity":2}}
        """


    def view_item_quantities(self) -> dict:
        """
        Return the current shopping list quantities of the items in the shopping list
        :return:dict, the current shopping list quantities of the items in the shopping list
        >>> shoppingcart.add_item_quantity("apple", 1, 5)
        >>> shoppingcart.add_item_quantity("banana", 2, 3)
        >>> shoppingcart.view_item_quantities()
        {"apple":{"price":1, "quantity":5}, "banana":{"price":2, "quantity":3}}
        """


    def total_price_quantity(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item_quantity("apple", 1, 5)
        >>> shoppingcart.add_item_quantity("banana", 2, 3)
        >>> shoppingcart.total_price_quantity()
        11.0
        """


    def quantities_quantity(self) -> dict:
        """
        Return the current shopping list quantities of the items in the shopping list
        :return:dict, the current shopping list quantities of the items in the shopping list
        >>> shoppingcart.add_item_quantity("apple", 1, 5)
        >>> shoppingcart.add_item_quantity("banana", 2, 3)
        >>> shoppingcart.quantities_quantity()
        {"apple":{"price":1, "quantity":5}, "banana":{"price":2, "quantity":3}}
        """


    def add_item_quantity_quantity(self, item, quantity, quantity_to_add):
        """
        Add the specified quantity of item to the shopping list items
        :param item:string, Item to be added
        :param quantity:int, Quantity to be added
        :param quantity_to_add:int, Quantity to add
        :return:None
        >>> shoppingcart =