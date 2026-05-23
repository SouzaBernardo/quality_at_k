class CurrencyConverter:
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """
        if from_currency not in self.rates:
            raise ValueError("Invalid currency")
        if to_currency not in self.rates:
            raise ValueError("Invalid currency")
        return self.rates[from_currency] * amount / self.rates[to_currency]

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency:string, currency type to be added
        :param rate:float, exchange rate for this type of currency
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        self.rates['KRW'] = 1308.84
        """
        if currency in self.rates:
            raise ValueError("Currency already exists")
        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
        if currency not in self.rates:
            raise ValueError("Currency does not exist")
        if new_rate <= 0:
            raise ValueError("New rate should be positive")
        self.rates[currency] = new_rate

# Instructions:
# 1. Implement the missing methods in the CurrencyConverter class
# 2. Test the class with the provided test cases
# 3. Add test cases for the new methods
# 4. Refactor the class to improve code readability and organization
# 5. Add more test cases to cover edge cases and error handling
# 6. Optimize the code for better performance
# 7. Document the class and its methods
# 8. Implement a main function to test the class
# 9. Add more functionality to the class as needed
# 10. Submit the code.