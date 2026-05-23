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
            x = str(x)
        if self.NUMBER in x:
            return x[self.NUMBER]
        elif self.NUMBER_TEEN in x:
            return x[self.NUMBER_TEEN]
        elif self.NUMBER_TEN in x:
            return x[self.NUMBER_TEN]
        elif self.NUMBER_MORE in x:
            return x[self.NUMBER_MORE]
        else:
            return ""

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        if x not in self.NUMBER:
            return ""
        if x not in self.NUMBER_TEEN:
            return ""
        if x not in self.NUMBER_TEN:
            return ""
        if x not in self.NUMBER_MORE:
            return ""

        word = self.NUMBER[x - self.NUMBER.index(x)]
        if self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "k":
            word = f"{word}k"
        elif self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "w":
            word = f"{word}w"
        elif self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "m":
            word = f"{word}m"
        elif self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "b":
            word = f"{word}b"
        elif self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "t":
            word = f"{word}t"
        elif self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "p":
            word = f"{word}p"
        elif self.NUMBER_SUFFIX[x - self.NUMBER.index(x)] == "e":
            word = f"{word}e"
        else:
            return "Invalid suffix"

        return f"{word} {x:.2f}"



    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        if s.startswith("k"):
            # Convert to lowercase
            s = s.lower()
        
        if s[-2:] == "k":
            # Add the suffix
            s += "k"
        
        if s[-2:] == "w":
            # Add the suffix
            s += "w"
        
        if s[-2:] == "m":
            # Add the suffix
            s += "m"
        
        if s[-2:] == "b":
            # Add the suffix
            s += "b"
        
        if s[-2:] == "t":
            # Add the suffix
            s += "t"
        
        if s[-2:] == "p":
            # Add the suffix
            s += "p"
        
        if s[-2:] == "e":
            # Add the suffix
            s += "e"
        
        return s

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        suffix = self.NUMBER_SUFFIX[i]
        if suffix == "k":
            return " thousand"
        elif suffix == "w":
            return " million"
        elif suffix == "m":
            return " billion"
        else:
            return None