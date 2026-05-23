
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
        """
        if isinstance(x, int):
            return self.format_string(x)
        elif isinstance(x, float):
            integer_part = int(x)
            decimal_part = x - integer_part
            integer_part_str = self.format_string(integer_part)
            decimal_part_str = ""
            if decimal_part > 0:
                decimal_part_str = " AND " + self.format_string(decimal_part)
            return integer_part_str + decimal_part_str


    def format_string(self, x):
        integer_part, decimal_part = x.split(".")
        integer_words = self.format(integer_part)
        decimal_words = self.format(decimal_part)
        if decimal_words:
            decimal_words = "AND " + decimal_words
        return integer_words + " ONLY" if not decimal_words else " ".join([integer_words, decimal_words])
    

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        if s[0] == "0":
            return self.NUMBER[int(s[1])]
        elif s[0] == "1":
            return self.NUMBER_TEEN[int(s[1])]
        else:
            return self.NUMBER_TEN[int(s[0]) - 1] + " " + self.NUMBER[int(s[1])]

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        if len(s)!= 3:
            return ""
        # Convert the first digit
        if s[0] == "0":
            result = ""
        elif s[0] == "1":
            result = self.NUMBER_TEEN[int(s[1])] + " "
        else:
            result = self.NUMBER[int(s[0])] + " HUNDRED "
        # Convert the second digit
        if s[1] == "0":
            result += ""
        elif s[1] == "1":
            result += self.NUMBER_TEEN[int(s[2])] + " "
        elif s[1] == "2":
            result += self.NUMBER_TEN[int(s[2])] + " "
        else:
            result += self.NUMBER_TEN[int(s[1])] + "-" + self.NUMBER[int(s[2])] + " "
        # Convert the third digit
        if s[2] == "0":
            result += ""
        else:
            result += self.NUMBER[int(s[2])] + " "
        return result.strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        return self.NUMBER_MORE[i]