
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
        if isinstance(x, int):
            return self.NUMBER[x]
        elif isinstance(x, float):
            return self.NUMBER_TEEN[x]
        else:
            return x


    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if x == "":
            return ""
        if x.isdigit():
            return self.NUMBER[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isdigit() or x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
        if x.isalpha():
            return self.NUMBER_SUFFIX[int(x)]
     

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        return self.NUMBER_SUFFIX[i]


    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        return self.NUMBER[int(s[0])] + self.NUMBER[int(s[1])] + self.NUMBER[int(s[2])]


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
        elif i == 1:
            return "THOUSAND"
        elif i == 2:
            return "MILLION"
        elif i == 3:
            return "BILLION"
        elif i == 4:
            return "THOUSAND"
        elif i == 5:
            return "MILLION"
        elif i == 6:
            return "BILLION"
        elif i == 7:
            return "THOUSAND"
        elif i == 8:
            return "MILLION"
        elif i == 9:
            return "BILLION"
        elif i == 10:
            return "THOUSAND"
        elif i == 11:
            return "MILLION"
        elif i == 12:
            return "BILLION"
        elif i == 13:
            return "THOUSAND"
        elif i == 14:
            return "MILLION"
        elif i == 15:
            return "BILLION"
        elif i == 16:
            return "THOUSAND"
        elif i == 17:
            return "MILLION"
        elif i == 18:
            return "BILLION"
        elif i == 19:
            return "THOUSAND"
        elif i == 20:
            return "MILLION"
        elif i == 21:
            return "BILLION"
        elif i == 22:
            return "THOUSAND"
        elif i == 23:
            return "MILLION"
        elif i == 24:
            return "BILLION"
        elif i == 25:
            return "THOUSAND"
        elif i == 26:
            return "MILLION"
        elif i == 27:
            return "BILLION"
        elif i == 28:
            return "THOUSAND"
        elif i == 29:
            return "MILLION"
        elif i == 30:
            return "BILLION"
        elif i == 31:
            return "THOUSAND"
        elif i == 32:
            return "MILLION"
        elif i == 33:
            return "BILLION"
        elif i == 34:
            return "THOUSAND"
        elif i == 35:
            return "MILLION"
        elif i == 36:
            return "BILLION"
        elif i == 37:
            return "THOUSAND"
        elif i == 38:
            return "MILLION"
        elif i == 39:
            return "BILLION"
        elif i == 40:
            return "THOUSAND"
        elif i == 41:
            return "MILLION"
        elif i == 42:
            return "BILLION"
        elif i == 43:
            return "THOUSAND"
        elif i == 44:
            return "MILLION"