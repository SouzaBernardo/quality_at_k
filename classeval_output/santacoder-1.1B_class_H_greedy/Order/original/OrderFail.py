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
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.checkout()
        32.0
        """


if __name__ == '__main__':
    order = Order()
    order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    order.menu.append({"dish": "dish2", "price": 20, "count": 3})
    order.menu.append({"dish": "dish3", "price": 30, "count": 2})
    order.menu.append({"dish": "dish4", "price": 40, "count": 1})
    order.menu.append({"dish": "dish5", "price": 50, "count": 1})
    order.menu.append({"dish": "dish6", "price": 60, "count": 1})
    order.menu.append({"dish": "dish7", "price": 70, "count": 1})
    order.menu.append({"dish": "dish8", "price": 80, "count": 1})
    order.menu.append({"dish": "dish9", "price": 90, "count": 1})
    order.menu.append({"dish": "dish10", "price": 100, "count": 1})
    order.menu.append({"dish": "dish11", "price": 110, "count": 1})
    order.menu.append({"dish": "dish12", "price": 120, "count": 1})
    order.menu.append({"dish": "dish13", "price": 130, "count": 1})
    order.menu.append({"dish": "dish14", "price": 140, "count": 1})
    order.menu.append({"dish": "dish15", "price": 150, "count": 1})
    order.menu.append({"dish": "dish16", "price": 160, "count": 1})
    order.menu.append({"dish": "dish17", "price": 170, "count": 1})
    order.menu.append({"dish": "dish18", "price": 180, "count": 1})
    order.menu.append({"dish": "dish19", "price": 190, "count": 1})
    order.menu.append({"dish": "dish20", "price": 200, "count": 1})
    order.menu.append({"dish": "dish21", "price": 210, "count": 1})
    order.menu.append({"dish": "dish22", "price": 220, "count": 1})
    order.menu.append({"dish": "dish23", "price": 230, "count": 1})
    order.menu.append({"dish": "dish24", "price": 240, "count": 1})
    order.menu.append({"dish": "dish25", "price": 250, "count": 1})
    order.menu.append({"dish": "dish26", "price": 260, "count": 1})
    order.menu.append({"dish": "dish27", "price": 270, "count": 1})
    order.menu.append({"dish": "dish28", "price": 280, "count": 1})
    order.menu.append({"dish": "dish29", "price": 290, "count": 1})
    order.menu.append({"dish": "dish30", "price": 300, "count": 1})
    order.menu.append({"dish": "dish31", "price": 310, "count": 1})
    order.menu.append({"dish": "dish32", "price": 320, "count": 1})
    order.menu.append({"dish": "dish33", "price": 330, "count": 1})
    order.menu.append({"dish": "dish34", "price": 340, "count": 1})
    order.menu.append({"dish": "dish35", "price": 350, "count": 1})
    order.menu.append({"dish": "dish36", "price": 360, "count": 1})
    order.menu.append({"dish": "dish37", "price": 370, "count": 1})
    order.menu.append({"dish": "dish38", "price": 380, "count": 1})
    order.menu.append({"dish": "dish39", "price": 390, "count": 1})
    order.menu.append({"dish": "dish40", "price": 400, "count": 1})
    order.menu.append({"dish": "dish41", "price": 410, "count": 1})
    order.menu.append({"dish": "dish42", "price": 420, "count": 1})
    order.menu.append({"dish": "dish43", "price": 430, "count": 1})
    order.menu.append({"dish": "dish44", "price": 440, "count": 1})
    order.menu.append({"dish": "dish45", "price": 450, "count": 1})
    order.menu.append({"dish": "dish46", "price": 460, "count": 1})
    order.menu.append({"dish": "dish47", "price": 470, "count": 1})
    order.