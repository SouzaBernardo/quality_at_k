class NumberWordFormatter: 
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
            return ""
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
            return "TWENTY"
        if x == 43:
            return "THIRTY"
        if x == 44:
            return "FORTY"
        if x == 45:
            return "FIFTY"
        if x == 46:


    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        return self.NUMBER[x.strip().lower()]


    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        return self.NUMBER_MORE[int(s[0:2])]


    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        return self.NUMBER[int(s)]


    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        if i == 0:
            return ""
        if i == 1:
            return "THOUSAND"
        if i == 2:
            return "MILLION"
        if i == 3:
            return "BILLION"
        if i == 4:
            return "THOUSAND"
        if i == 5:
            return "MILLION"
        if i == 6:
            return "BILLION"
        if i == 7:
            return "THOUSAND"
        if i == 8:
            return "MILLION"
        if i == 9:
            return "BILLION"
        if i == 10:
            return "THOUSAND"
        if i == 11:
            return "MILLION"
        if i == 12:
            return "BILLION"
        if i == 13:
            return "THOUSAND"
        if i == 14:
            return "MILLION"
        if i == 15:
            return "BILLION"
        if i == 16:
            return "THOUSAND"
        if i == 17:
            return "MILLION"
        if i == 18:
            return "BILLION"
        if i == 19:
            return "THOUSAND"
        if i == 20:
            return "MILLION"
        if i == 21:
            return "BILLION"
        if i == 22:
            return "THOUSAND"
        if i == 23:
            return "MILLION"
        if i == 24:
            return "BILLION"
        if i == 25:
            return "THOUSAND"
        if i == 26:
            return "MILLION"
        if i == 27:
            return "BILLION"
        if i == 28:
            return "THOUSAND"
        if i == 29:
            return "MILLION"
        if i == 30:
            return "BILLION"
        if i == 31:
            return "THOUSAND"
        if i == 32:
            return "MILLION"
        if i == 33:
            return "BILLION"
        if i == 34:
            return "THOUSAND"
        if i == 35:
            return "MILLION"
        if i == 36:
            return "BILLION"
        if i == 37:
            return "THOUSAND"
        if i == 38:
            return "MILLION"
        if i == 39:
            return "BILLION"
        if i == 40:
            return "THOUSAND"
        if i == 41:
            return "MILLION"
        if i == 42:
            return "BILLION"
        if i == 43:
            return "THOUSAND"
        if i == 44:
            return "MILLION"