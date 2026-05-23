
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
        "ONE HUNDRED AND TWENTY THREE MILLION FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if type(x) == int:
            x = float(x)
        words = ""
        if x == 0:
            words = "ZERO"
        else:
            whole, decimal = str(x).split(".")
            whole = int(whole)
            decimal = int (decimal)
            words = self.format_integer(whole) + " ONLY"
            if decimal!= 0:
                words += " AND " + self.format_decimal(decimal)
        return words


    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        words = ""
        if x == "0":
            words = "ZERO"
        else:
            whole, decimal = x.split(".")
            whole = int(whole)
            decimal = int (decimal)
            words = self.format_integer(whole) + " ONLY"
            if decimal!= 0:
                words += " AND " + self.format_decimal(decimal)
        return words

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        words = ""
        if s[0] == '0':
            words = self.NUMBER[int(s[1])]
        else:
            words = self.NUMBER[int(s[0])] + " " + self.NUMBER[int(s[1])]
        return words

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        words = ""
        if s[0] == '0':
            if s[1] == '0':
                words = self.NUMBER_TEEN[int(s[2])]
            else:
                words = self.NUMBER[int(s[1])] + " " + self.NUMBER_TEEN[int(s[2])]
        else:
            if s[1] == '0':
                words = self.NUMBER[int(s[0])] + " HUNDRED AND " + self.NUMBER_TEN[int(s[2])]
            else:
                words = self.NUMBER[int(s[0])] + " HUNDRED AND " + self.NUMBER[int(s[1])] + " " + self.NUMBER_TEN[int(s[2])]
        return words

