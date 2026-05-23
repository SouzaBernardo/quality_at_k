
class Order:  
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """

    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
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
        dish_name = dish["dish"]
        dish_price = dish["price"]
        dish_count = dish["count"]
        dish_exist = False
        for dish in self.menu:
            if dish["dish"] == dish_name:
                dish_exist = True
                dish["count"] = dish_count + 1
                break
        if not dish_exist:
            self.menu.append({"dish": dish_name, "price": dish_price, "count": dish_count + 1})
            self.selected_dishes.append(dish)
            return True
        else:
            return False

