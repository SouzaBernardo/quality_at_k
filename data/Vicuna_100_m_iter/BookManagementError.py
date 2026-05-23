class BookManagement:  
    """
    This is a class as managing books system, which supports to add and remove books from the inventory dict, view the inventory, and check the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}



    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
    
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
        if title in self.inventory:
            if quantity > 1:
                self.inventory[title] = quantity
            else:
                self.inventory[title] += 1
        else:
            self.inventory[title] = quantity
    
        self.print_inventory()

    def remove_book(self, title, quantity):
        if title in self.inventory:
            if quantity > 0:
                if quantity == 1:
                    del self.inventory[title]
                else:
                    self.inventory[title] -= quantity
            else:
                raise ValueError("Invalid book title")
    
            self.print_inventory()