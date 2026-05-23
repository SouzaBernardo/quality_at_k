
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
        """
        if stock in self.portfolio:
            self.portfolio.remove(stock)
            return True
        else:
            return False
    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        total_price = stock['price'] * stock['quantity']
        if self.cash_balance >= total_price:
            self.cash_balance -= total_price
            self.add_stock(stock)
            return True
        else:
            return False
    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was sold successfully, False if the stock is not in the portfolio.
        """
        if stock in self.portfolio:
            self.cash_balance += stock['price'] * stock['quantity']
            self.remove_stock(stock)
            return True
        else:
            return False
    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value
    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = self.calculate_portfolio_value()
        portfolio_summary = []
        for stock in self.portfolio:
            stock_value = stock['price'] * stock['quantity']
            portfolio_summary.append({'name': stock['name'], 'value': stock_value})
        return total_value, portfolio_summary
    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        return stock['price'] * stock['quantity']
