class Order: 
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
        >>> order.selected_dishes.append({"dish": "dish1", "count": 3, price: 10})
        True
        """
        if dish in self.menu and self.selected_dishes[ dish ] and self.selected_dishes[ dish ]['count']!= self.selected_dishes[ dish ]['count']:
            self.selected_dishes[ dish ]['count'] += 1
            self.sales[ dish ] = self.calculate_total(self.sales[ dish ])
        else:
            self.selected_dishes[ dish ] = {'count': self.selected_dishes[ dish ]['count'], 'price': self.calculate_total(self.sales[ dish ])}



    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        """
        if self.selected_dishes:
            total = self.calculate_total()
            if total:
                self.sales[self.selected_dishes[0]] = total
                return total
        return False