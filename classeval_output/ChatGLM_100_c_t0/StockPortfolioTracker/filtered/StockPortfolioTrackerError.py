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
        """
        self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": stock["quantity"]})

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        for item in self.portfolio:
            if item["name"] == stock["name"] and item["quantity"] == stock["quantity"]:
                self.portfolio.remove(item)
                break
        else:
            print(f"{stock['name']} is not in the portfolio")

    def buy_stock(self, stock, quantity):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        if stock["name"] == "AAPL" and quantity > 10:
            self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": quantity})
            self.cash_balance += quantity
            return True
        else:
            print(f"{stock['name']} is not a stock")
            return False

    def sell_stock(self, stock, quantity):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        if stock["name"] == "AAPL" and quantity > 10:
            self.portfolio.append({"name": stock["name"], "price": stock["price"], "quantity": quantity})
            self.cash_balance -= quantity
            return True
        else:
            print(f"{stock['name']} is not a stock")
            return False

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = 0.0
        for item in self.portfolio:
            total_value += item["price"]
        return total_value

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        return (total_value, [
            {'name': stock["name"], 'value': stock["value"]}
            for stock in self.portfolio
        ])

    def get_stock_value(self, stock):