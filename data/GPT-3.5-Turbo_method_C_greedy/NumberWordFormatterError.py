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
        x_str = str(x)
        integer_part, decimal_part = x_str.split(".")
        words = []
    
        if integer_part != "0":
            words.append(self.trans_three(integer_part))
    
        if decimal_part != "0":
            words.append(self.trans_two(decimal_part))
    
        if integer_part != "0" and decimal_part != "0":
            words.append("AND")
    
        result = " ".join(words) + " ONLY"
        return result
    



    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        tens_digit = int(s[0])
        ones_digit = int(s[1])
    
        if tens_digit == 1:
            return self.NUMBER_TEEN[ones_digit]
        else:
            return self.NUMBER_TEN[tens_digit - 1] + " " + self.NUMBER[ones_digit]
    

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        result = ""
        if s[0] != "0":
            result += self.NUMBER[int(s[0])] + " HUNDRED"
            if s[1:] != "00":
                result += " AND "
        result += self.trans_two(s[1:])
        return result
    

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        return self.NUMBER_MORE[i]