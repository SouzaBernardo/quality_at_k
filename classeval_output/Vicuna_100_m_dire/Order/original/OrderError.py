
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
        if dish not in self.menu:
            self.menu.append(dish)
        if dish in self.selected_dishes:
            self.selected_dishes.remove(dish)
        else:
            self.selected_dishes.append(dish)
        self.sales[dish['dish']] = dish['price'] * dish['count']
        return True

    def calculate_total(self):
        total = 0.0
        for dish in self.selected_dishes:
            if dish in self.sales:
                total += self.sales[dish] * self.selected_dishes[dish]["count"]
        return total

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
        if not self.selected_dishes:
            return False
        total = 0
        for dish in self.selected_dishes:
            total += self.sales[dish]['price'] * self.sales[dish]['count']
        return total