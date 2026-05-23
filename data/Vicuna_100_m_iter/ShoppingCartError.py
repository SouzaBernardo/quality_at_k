class ShoppingCart:  
    """
    The class manages items, their prices, quantities, and allows to for add, removie, view items, and calculate the total price.
    """

    def __init__(self):
        """
        Initialize the items representing the shopping list as an empty dictionary
        """
        self.items = {}






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
        if item in self.items:
            if quantity > 0:
                self.items[item]["quantity"] -= quantity
                if self.items[item]["quantity"] <= 0:
                    del self.items[item]
            else:
                raise ValueError("Quantity must be a positive integer.")
        else:
            raise ValueError("Item not found.")

    def view_items(self) -> dict:
        """
        Return the current shopping list items
        :return:dict, the current shopping list items
        """
        return self.items

    def total_price(self) -> float:
        """
        Calculate the total price of all items in the shopping list, which is the quantity of each item multiplied by the price
        :return:float, the total price of all items in the shopping list
        """
        total_price = 0.0
        for item, quantity in self.items.items():
            price = self.items[item]["price"]
            total_price += price * quantity
        return total_price