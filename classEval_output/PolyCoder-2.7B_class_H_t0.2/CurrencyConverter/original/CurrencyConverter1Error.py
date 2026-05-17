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


    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """


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


    def get_currency_rate(self, currency):
        """
        Get the exchange rate for a certain currency
        :param currency:string, currency type to be checked
        :return:float, exchange rate for this currency type
        >>> cc = CurrencyConverter()
        >>> cc.get_currency_rate('USD')
        1.0
        >>> cc.get_currency_rate('EUR')
        0.85
        >>> cc.get_currency_rate('GBP')
        0.72
        >>> cc.get_currency_rate('JPY')
        110.15
        >>> cc.get_currency_rate('CAD')
        1.23
        >>> cc.get_currency_rate('AUD')
        1.34
        >>> cc.get_currency_rate('CNY')
        7.18
        """


    def get_supported_currencies(self):
        """
        Returns a list of supported currencies
        :return:list, All supported currencies
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """


    def get_supported_currencies_for_currency(self, currency):
        """
        Returns a list of supported currencies for a given currency
        :param currency:string, currency type to be checked
        :return:list, All supported currencies for this currency type
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies_for_currency('USD')
        ['USD']
        >>> cc.get_supported_currencies_for_currency('EUR')
        ['EUR']
        >>> cc.get_supported_currencies_for_currency('GBP')
        ['GBP']
        >>> cc.get_supported_currencies_for_currency('JPY')
        ['JPY']
        >>> cc.get_supported_currencies_for_currency('CAD')
        ['CAD']
        >>> cc.get_supported_currencies_for_currency('AUD')
        ['AUD']
        >>> cc.get_supported_currencies_for_currency('CNY')
        ['CNY']
        """


    def get_supported_currencies_for_currency_type(self, currency_type):
        """
        Returns a list of supported currencies for a given currency type
        :param currency_type:string, currency type to be checked
        :return:list, All supported currencies for this currency type
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies_for_currency_type('USD')
        ['USD']
        >>> cc.get_supported_currencies_for_currency_type('EUR')
        ['EUR']
        >>> cc.get_supported_currencies_for_currency_type('GBP')
        ['GBP']
        >>> cc.get_supported_currencies_for_currency_type('JPY')
        ['JPY']
        >>> cc.get_supported_currencies_for_currency_type('CAD')
        ['CAD']
        >>> cc.get_supported_currencies_for_currency_type('AUD')
   