
class BookManagement: 
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
            if quantity > 0:
                self.inventory[title] += quantity
            else:
                self.inventory[title] = 1
        else:
            self.inventory[title] = quantity


    def remove_book(self, title, quantity):
        if not title:
            raise ValueError("Invalid input, please provide a book title.")
        if not quantity:
            raise ValueError("Invalid input, please provide a quantity.")
        if title not in self.inventory:
            raise ValueError("Invalid book title, book not found.")
        del self.inventory[title]
        if quantity > 0:
            for key, value in self.inventory.items():
                if key != title:
                    self.inventory[key] -= quantity
        else:
            self.inventory[title] -= quantity

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
        return self.inventory

    def view_book_quantity(self, title):
        if title in self.inventory:
            return self.inventory[title]
        else:
            return 0