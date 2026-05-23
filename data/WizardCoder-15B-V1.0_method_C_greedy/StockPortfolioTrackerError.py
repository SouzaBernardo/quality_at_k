class StockPortfolioTracker: 
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
        """
        self.portfolio.append(stock)

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []
        """
        for i in range(len(self.portfolio)):
            if self.portfolio[i]['name'] == stock['name'] and self.portfolio[i]['price'] == stock['price'] and self.portfolio[i]['quantity'] == stock['quantity']:
                self.portfolio.pop(i)
                return True
        return False

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        total_cost = stock["price"] * stock["quantity"]
        if total_cost > self.cash_balance:
            return False
        else:
            self.cash_balance -= total_cost
            self.portfolio.append(stock)
            return True

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        for s in self.portfolio:
            if s['name'] == stock['name']:
                if s['quantity'] >= stock['quantity']:
                    s['quantity'] -= stock['quantity']
                    self.cash_balance += stock['price'] * stock['quantity']
                    return True
                else:
                    return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = 0.0
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = 0
        stock_values = []
        for stock in self.portfolio:
            stock_value = self.get_stock_value(stock)
            stock_values.append({'name': stock['name'], 'value': stock_value})
            total_value += stock_value
        total_value += self.cash_balance
        return total_value, stock_values

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        return stock["price"] * stock["quantity"]