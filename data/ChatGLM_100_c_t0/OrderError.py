def has_selected_dishes(self):
    """
    Check if the customer has selected any dishes.
    :return: True if the customer has selected dishes, False otherwise.
    """
    return self.selected_dishes.count == 0


def calculate_total_cost(self):
    """
    Calculate the total cost of the orders.
    :return total: float, the final total cost.
    """
    return sum([self.sales.get(d, 0) for d in self.menu])


def check_and_calculate_total_cost(self):
    """
    Check if the customer has selected any dishes and calculate the total cost.
    :return: True if the customer has selected dishes and total(return value of calculate_total) otherwise.
    """
    if self.has_selected_dishes():
        self.calculate_total()
    else:
        return False


def add_dish(self, dish):
    """
    Add the specified dish to the order.
    :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
    :return: True if successfully added, or False otherwise.
    """
    if dish.count == 0:
        return False
    self.selected_dishes[ dish.dish ] = { dish.dish: dish.count, dish.price: dish.price }
    return True


class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count},...]
        self.selected_dishes stores the dished selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}

    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        """
        if dish.count == 0:
            return False
        self.selected_dishes[ dish.dish ] = { dish.dish: dish.count, dish.price: dish.price }
        self.sales[ dish.dish ] = 0
        return True

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        """
        return sum([self.sales.get(d, 0) for d in self.menu])

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        """
        if self.has_selected_dishes():
            self.calculate_total()
        else:
            return False

    def check_and_calculate_total_cost(self):
        """
        Check if the customer has selected any dishes and calculate the total cost.
        :return: True if the customer has selected dishes and total(return value of calculate_total) otherwise.
        """
        if self.has_selected_dishes():
            self.calculate_total_cost()
        else:
            return False

    def add_dish(self, dish):
        """
        Add the specified dish to the order.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        """