class StockPortfolioTracker:  
    """
    This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.portfolio = []
        self.cash_balance = cash_balance



    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was removed, False otherwise
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                self.portfolio.remove(s)
                return True
        return False

    def buy_stock(self, stock, quantity):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if self.cash_balance >= stock['price'] * quantity:
            self.portfolio.append({'name': stock['name'], 'price': stock['price'], 'quantity': quantity})
            self.cash_balance -= stock['price'] * quantity
            return True
        else:
            return False

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                self.portfolio.remove(s)
                self.cash_balance += stock['price'] * s['quantity']
                return True
        return False
        """

    def calculate_portfolio_value(self):
        """
        :return: the total value of the portfolio, float.
        """
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        """
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = self.cash_balance
        stock_list = []
        for stock in self.portfolio:
            stock_list.append({'name': stock['name'], 'value': stock['price'] * stock['quantity']})
            total_value += stock['price'] * stock['quantity']
        return total_value, stock_list

    def get_stock_value(self, stock):
        """
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        for s in self.portfolio:
            if s['name'] == stock['name'] and s['price'] == stock['price'] and s['quantity'] == stock['quantity']:
                return s['price'] * s['quantity']
        return 0