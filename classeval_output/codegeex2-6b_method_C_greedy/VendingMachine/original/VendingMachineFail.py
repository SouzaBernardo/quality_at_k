
class VendingMachine: 
    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0



    def add_item(self, item_name, price, quantity):
        
        self.inventory[item_name] = {'price': price, 'quantity': quantity}


    def insert_coin(self, amount):
        

        self.balance += amount
        return self.balance


    def purchase_item(self, item_name):


    def restock_item(self, item_name, quantity):


    def display_items(self):
