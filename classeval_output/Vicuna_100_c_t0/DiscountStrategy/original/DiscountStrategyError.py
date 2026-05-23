To complete the class DiscountStrategy, you need to add the following methods:

1. `due()`: This method should calculate the final amount to be paid after applying the discount.
2. `due(order)`: This method should calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
3. `due(order)`: This method should calculate the discount based on bulk item quantity in the order.In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
4. `due(order)`: This method should calculate the discount based on the number of different products in the order.If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.

Here is the implementation for the `due()` method:
```python
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart)
        >>> ds.due()
        312.55

        """
        total_cost = sum([item['price'] * item['quantity'] for item in self.cart])
        discount = 0.0
        if self.customer.get('fidelity', 0) >= 1000:
            discount = 0.05 * total_cost
        if self.cart[0]['quantity'] >= 20:
            discount = (self.cart[0]['quantity'] * 0.1) * total_cost
        if len(self.cart) > 1 and self.cart[0]['product'] != self.cart[1]['product']:
            discount = (len(self.cart) * 0.07) * total_cost
        return total_cost - discount
```
You can add the other methods in a similar way.