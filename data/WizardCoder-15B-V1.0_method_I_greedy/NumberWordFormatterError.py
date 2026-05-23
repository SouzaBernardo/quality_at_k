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
        """
        if isinstance(x, int):
            x = str(x)
        elif isinstance(x, float):
            x = str(x)[:7]
        else:
            return "Invalid input type"
        integer_part = x.split(".")[0]
        decimal_part = x.split(".")[1]
        integer_words = self.convert_integer(integer_part)
        decimal_words = self.convert_decimal(decimal_part)
        if decimal_words:
            return integer_words + " AND " + decimal_words + " ONLY"
        else:
            return integer_words

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        if isinstance(x, int):
            x = str(x)
        elif isinstance(x, float):
            x = str(x)[:7]
        else:
            return "Invalid input type"
        integer_part = x.split(".")[0]
        decimal_part = x.split(".")[1]
        integer_words = self.convert_integer(integer_part)
        decimal_words = self.convert_decimal(decimal_part)
        if decimal_words:
            return integer_words + " AND " + decimal_words + " ONLY"
        else:
            return integer_words

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        if len(s)!= 2:
            return "Invalid input"
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            tens = num // 10
            ones = num % 10
            if ones == 0:
                return self.NUMBER_TEN[tens - 1]
            else:
                return self.NUMBER_TEN[tens - 1] + " " + self.NUMBER[ones]



    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        if i == 0:
            return ""
        elif i == 1:
            return "THOUSAND"
        elif i == 2:
            return "MILLION"
        elif i == 3:
            return "BILLION"
        else:
            return ""