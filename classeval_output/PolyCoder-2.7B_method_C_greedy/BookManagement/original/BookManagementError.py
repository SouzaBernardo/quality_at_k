
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
        self.inventory[title] = quantity


    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        if title not in self.inventory:
            raise ValueError("The book title is not in the inventory")
        if quantity < 1:
            raise ValueError("The quantity of the book is less than 1")
        if quantity > len(self.inventory[title]):
            raise ValueError("The quantity of the book is greater than the number of books in the inventory")
        self.inventory[title].remove(quantity)
        self.inventory[title] = sorted(self.inventory[title], key=lambda x: x[1])
        self.inventory[title] = self.inventory[title][0:quantity]
        self.inventory[title] = self.inventory[title][quantity:]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
        self.inventory[title] = self.inventory[title][0:len(self.inventory[title])]
        self.inventory[title] = self.inventory[title][len(self.inventory[title]):]
     

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int),...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
        return self.inventory


    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        """
        pass
