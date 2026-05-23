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
            return "ZERO"
        if x < 0:
            return "NEGATIVE " + self.format(-x)
        if x < 20:
            return self.NUMBER[x]
        if x < 100:
            if x % 10 == 0:
                return self.NUMBER_TEEN[x // 10] + " " + self.NUMBER_MORE[x % 10]
            else:
                return self.NUMBER_TEN[x // 10] + " " + self.NUMBER_MORE[x % 10]
        if x < 1000:
            if x % 100 == 0:
                return self.NUMBER_TEN[x // 100] + " " + self.NUMBER_MORE[x % 100]
            elif x % 10 == 0:
                return self.NUMBER_TEEN[x // 10] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 100]
            else:
                return self.NUMBER_TEN[x // 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 10]
        if x < 1000000:
            if x % 1000 == 0:
                return self.NUMBER_TEN[x // 1000] + " " + self.NUMBER_MORE[x % 1000]
            elif x % 100 == 0:
                return self.NUMBER_TEN[x // 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 1000]
            elif x % 10 == 0:
                return self.NUMBER_TEN[x // 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 10]
            else:
                return self.NUMBER_TEN[x // 1000] + " " + self.NUMBER_MORE[x % 1000] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 100]
        if x < 1000000000:
            if x % 1000000 == 0:
                return self.NUMBER_TEN[x // 1000000] + " " + self.NUMBER_MORE[x % 1000000]
            elif x % 100000 == 0:
                return self.NUMBER_TEN[x // 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000]
            elif x % 10000 == 0:
                return self.NUMBER_TEN[x // 10000] + " " + self.NUMBER_MORE[x % 10000] + " " + self.NUMBER_MORE[x % 10000] + " " + self.NUMBER_MORE[x % 10000]
            elif x % 1000 == 0:
                return self.NUMBER_TEN[x // 1000] + " " + self.NUMBER_MORE[x % 1000] + " " + self.NUMBER_MORE[x % 1000] + " " + self.NUMBER_MORE[x % 1000] + " " + self.NUMBER_MORE[x % 1000]
            elif x % 100 == 0:
                return self.NUMBER_TEN[x // 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 100] + " " + self.NUMBER_MORE[x % 100]
            elif x % 10 == 0:
                return self.NUMBER_TEN[x // 10] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 10] + " " + self.NUMBER_MORE[x % 10]
            else:
                return self.NUMBER_TEN[x // 1000000] + " " + self.NUMBER_MORE[x % 1000000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " + self.NUMBER_MORE[x % 100000] + " " +