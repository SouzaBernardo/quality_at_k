
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
        self.portfolio.append(stock)
    

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        """
        self.portfolio.remove(stock)
        return True
    

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        """
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]
        total_cost = stock_price * stock_quantity
    
        if total_cost <= self.cash_balance:
            self.portfolio.append(stock)
            self.cash_balance -= total_cost
            return True
        else:
            return False
    

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        """
        stock_name = stock["name"]
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]
    
        for item in self.portfolio:
            if item["name"] == stock_name:
                if item["quantity"] >= stock_quantity:
                    item["quantity"] -= stock_quantity
                    self.cash_balance += stock_price * stock_quantity
                    if item["quantity"] == 0:
                        self.portfolio.remove(item)
                    return True
                else:
                    return False
    
        return False
    

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        """
        total_value = self.cash_balance
    
        for stock in self.portfolio:
            stock_price = stock["price"]
            stock_quantity = stock["quantity"]
            stock_value = stock_price * stock_quantity
            total_value += stock_value
    
        return total_value
    

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        """
        total_value = self.calculate_portfolio_value()
        stock_summary = []
    
        for stock in self.portfolio:
            stock_name = stock["name"]
            stock_price = stock["price"]
            stock_quantity = stock["quantity"]
            stock_value = stock_price * stock_quantity
    
            stock_dict = {"name": stock_name, "value": stock_value}
            stock_summary.append(stock_dict)
    
        return total_value, stock_summary
    

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        """
        stock_price = stock["price"]
        stock_quantity = stock["quantity"]
        stock_value = stock_price * stock_quantity
    
        return stock_value
    