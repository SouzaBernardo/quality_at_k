class VendingMachine: 
    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0



    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added, str.
        :param price: The price of the product to be added, float.
        :param quantity: The quantity of the product to be added, int.
        :return: None
        """
        self.inventory[item_name] = {'price': price, 'quantity': quantity}
    

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        """
        self.balance += amount
        return self.balance
    

    def purchase_item(self, item_name):
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] > 0:
                if self.balance >= self.inventory[item_name]['price']:
                    self.balance -= self.inventory[item_name]['price']
                    self.inventory[item_name]['quantity'] -= 1
                    return self.balance
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            return False
    

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        """
        if not self.inventory:
            return False
        else:
            items = []
            for item_name, item_info in self.inventory.items():
                price = item_info['price']
                quantity = item_info['quantity']
                items.append(f"{item_name} - ${price} [{quantity}]")
            return ", ".join(items)