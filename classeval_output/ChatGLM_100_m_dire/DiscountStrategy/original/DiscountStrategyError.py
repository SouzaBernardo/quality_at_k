
class DiscountStrategy: 
    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, customer information
        :param cart: list of dicts, a cart of items with details
        :param promotion: function, optional promotion applied to the order
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)

        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.total()



    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        """
        total = 0.0
        for item in self.cart:
            total += item['price']
        return total



    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        if order.get('fidelity') >= 1000:
            discount = order.get('price') * 0.05
            order.set('price', discount)
            return discount
        else:
            return None

    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        if order.quantity > 20 or order.quantity == 0:
            return 0.1
        else:
            return order.quantity * 0.1

    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        total_quantity = order.total()
        if total_quantity >= 10:
            discount = (total_quantity * 0.07) * 100
            order.total -= discount
            return discount
        else:
            return None