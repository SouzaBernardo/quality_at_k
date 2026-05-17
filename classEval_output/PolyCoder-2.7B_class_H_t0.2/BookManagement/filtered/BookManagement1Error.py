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

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """

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

    def check_book_quantity(self, title, quantity):
        """
        Check if the quantity of a book is valid.
        :param title: str, the title of the book.
        :param quantity: int, the quantity of the book.
        :return bool: True if the quantity of the book is valid, False otherwise.
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        True
        >>> bookManagement.check_book_quantity("book1", 1)
        False
        """

    def get_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        >>> bookManagement.get_book_quantity("book1")
        1
        """

    def check_book_quantity_exist(self, title, quantity):
        """
        Check if the quantity of a book is exist.
        :param title: str, the title of the book.
        :param quantity: int, the quantity of the book.
        :return bool: True if the quantity of the book is exist, False otherwise.
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        True
        >>> bookManagement.check_book_quantity_exist("book1", 1)
        False
        """

    def get_book_quantity_exist(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        >>> bookManagement.get_book_quantity_exist("book1")
        1
        """

    def add_book_to_inventory(self, title, quantity):
        """
        Add a book to inventory.
        :param title: str, the title of the book.
        :param quantity: int, the quantity of the book.
        :return self.inventory: dictionary, {title(str): quantity(int),...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.add_book("book3", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1, 'book3': 1}
        """

    def remove_book_from_inventory(self, title, quantity):
        """
        Remove a book from inventory.
        :param title: str, the title of the book.
        :param quantity: int, the quantity of the book.
        :return self.inventory: dictionary, {title(str): quantity(int),...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.add_book("book3", 1)
        >>> bookManagement.remove_book_from_inventory("book1", 1)
        >>> bookManagement.view_inventory()
        {'book2': 1, 'book3': 1}
        """

    def view_inventory_of_book(self, title):
        """
        Get the inventory of a book.
        :param title: str, the title of the book.