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


    def get_price(self, item, quantity=1) -> float:
        """
        Calculate the price of the item in the shopping list, which is the quantity of the item multiplied by the price
        :param item:string, Item to be calculated
        :param quantity:int, The number of items, defaults to 1
        :return:float, the price of the item in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        >>> shoppingcart.get_price("apple")
        11.0
        >>> shoppingcart.get_price("banana")
        11.0
        """


    def get_quantity(self, item, price=1) -> int:
        """
        Calculate the quantity of the item in the shopping list, which is the number of items multiplied by the price
        :param item:string, Item to be calculated
        :param price:float, The price of the item
        :return:int, the quantity of the item in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        >>> shoppingcart.get_quantity("apple")
        3
        >>> shoppingcart.get_quantity("banana")
        2
        """


    def get_total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        >>> shoppingcart.get_total_price()
        11.0
        """


    def add_item_to_cart(self, item, quantity=1):
        """
        Add item to the shopping list, which is the quantity of the item multiplied by the price
        :param item:string, Item to be added
        :param quantity:int, The number of items, defaults to 1
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        >>> shoppingcart.add_item_to_cart("apple", 3)
        >>> shoppingcart.total_price()
        11.0
        """


    def remove_item_from_cart(self, item, quantity=1):
        """
        Subtract item from the shopping list, which is the quantity of the item multiplied by the price
        :param item:string, Item to be subtracted
        :param quantity:int, The number of items, defaults to 1
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)