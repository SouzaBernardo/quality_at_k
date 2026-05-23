class ShoppingCart: 
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
        """
        if item in self.items:
            if self.items[item]["quantity"] >= quantity:
                self.items[item]["quantity"] -= quantity
                if self.items[item]["quantity"] == 0:
                    del self.items[item]
            else:
                raise ValueError("Quantity to be removed exceeds the available quantity")
        else:
            raise ValueError("Item not found in the shopping list")

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
        total = 0
        for item in self.items:
            total += self.items[item]["price"] * self.items[item]["quantity"]
        return total