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
        :param currency:string
        :return:float, exchange rate for this currency
        >>> cc = CurrencyConverter()
        >>> cc.get_currency_rate('KRW')
        1308.84
        """


    def get_currency_rates(self):
        """
        Get the exchange rates for all currencies
        :return:list, list of exchange rates for all currencies
        >>> cc = CurrencyConverter()
        >>> cc.get_currency_rates()
        ['KRW', 'CNY']
        """


    def get_currency_rate_by_name(self, name):
        """
        Get the exchange rate for a certain currency
        :param name:string
        :return:float, exchange rate for this currency
        >>> cc = CurrencyConverter()
        >>> cc.get_currency_rate_by_name('KRW')
        1308.84
        """


    def get_currency_rates_by_name(self, name):
        """
        Get the exchange rates for a certain currency
        :param name:string
        :return:list, list of exchange rates for this currency
        >>> cc = CurrencyConverter()
        >>> cc.get_currency_rates_by_name('KRW')
        ['KRW', 'CNY']
        """


    def get_supported_currencies_by_name(self, name):
        """
        Get the supported currencies for a certain currency
        :param name:string
        :return:list, list of supported currencies for this currency
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies_by_name('KRW')
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """


    def get_supported_currencies_by_name_and_rate(self, name, rate):
        """
        Get the supported currencies for a certain currency
        :param name:string
        :param rate:float
        :return:list, list of supported currencies for this currency
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies_by_name_and_rate('KRW', 1308.84)
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """


    def get_supported_currencies_by_name_and_rate_and_currency(self, name, rate, currency):
        """
        Get the supported currencies for a certain currency
        :param name:string
        :param rate:float
        :param currency:string
        :return:list, list of supported currencies for this currency
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies_by_name_and_rate_and_currency('KRW', 1308.84, 'USD')
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """


    def get_supported_currencies_by_name_and_rate_and_currency_and_currency(self, name, rate, currency, currency_from_currency):
        """