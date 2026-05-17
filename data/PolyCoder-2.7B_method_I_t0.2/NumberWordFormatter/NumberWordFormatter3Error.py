class NumberWordFormatter:  
    """
    This is a class that provides to convert numbers into their corresponding English word representation, including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN",
                            "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]



    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if x == 0:
            return "0"
        if x == 1:
            return "ONE"
        if x == 2:
            return "TWO"
        if x == 3:
            return "THREE"
        if x == 4:
            return "FOUR"
        if x == 5:
            return "FIVE"
        if x == 6:
            return "SIX"
        if x == 7:
            return "SEVEN"
        if x == 8:
            return "EIGHT"
        if x == 9:
            return "NINE"
        if x == 10:
            return "TEN"
        if x == 11:
            return "ELEVEN"
        if x == 12:
            return "TWELVE"
        if x == 13:
            return "THIRTEEN"
        if x == 14:
            return "FOURTEEN"
        if x == 15:
            return "FIFTEEN"
        if x == 16:
            return "SIXTEEN"
        if x == 17:
            return "SEVENTEEN"
        if x == 18:
            return "EIGHTEEN"
        if x == 19:
            return "NINETEEN"
        if x == 20:
            return "TEN"
        if x == 21:
            return "ELEVEN"
        if x == 22:
            return "TWENTY"
        if x == 23:
            return "THIRTY"
        if x == 24:
            return "FORTY"
        if x == 25:
            return "FIFTY"
        if x == 26:
            return "SIXTY"
        if x == 27:
            return "SEVENTY"
        if x == 28:
            return "EIGHTY"
        if x == 29:
            return "NINETY"
        if x == 30:
            return "TEN"
        if x == 31:
            return "ELEVEN"
        if x == 32:
            return "TWENTY"
        if x == 33:
            return "THIRTY"
        if x == 34:
            return "FORTY"
        if x == 35:
            return "FIFTY"
        if x == 36:
            return "SIXTY"
        if x == 37:
            return "SEVENTY"
        if x == 38:
            return "EIGHTY"
        if x == 39:
            return "NINETY"
        if x == 40:
            return "TEN"
        if x == 41:
            return "ELEVEN"
        if x == 42:
            return "TWELVE"
        if x == 43:
            return "THIRTEEN"
        if x == 44:
            return "FOURTEEN"
        if x == 45:
            return "FIFTEEN"
        if x == 46:
            return "SIXTEEN"
        if x == 47:
            return "SEVENTEEN"
        if x == 48:
            return "EIGHTEEN"