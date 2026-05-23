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
            return self._convert_integer(x)
        elif isinstance(x, float):
            return self._convert_float(x)
        else:
            raise ValueError("Input must be an integer or float")
    
    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        try:
            x = float(x)
            if x.is_integer():
                return self._convert_integer(int(x))
            else:
                return self._convert_float(x)
        except ValueError:
            raise ValueError("Input must be a string representation of a number")
    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        if len(s) != 2:
            raise ValueError("Input must be a two-digit number")
    
        first_digit, second_digit = int(s[0]), int(s[1])
    
        if first_digit == 1:
            return self.NUMBER_TEEN[second_digit]
        else:
            return self.NUMBER_TEN[first_digit - 1] + " " + self.NUMBER[second_digit]
    
    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        if len(s) != 3:
            raise ValueError("Input must be a three-digit number")
    
        first_digit, second_digit, third_digit = int(s[0]), int(s[1]), int(s[2])
    
        if first_digit == 0:
            return self.trans_two(s[1:])
        else:
            if second_digit == 0 and third_digit == 0:
                return self.NUMBER[first_digit] + " HUNDRED"
            else:
                return self.NUMBER[first_digit] + " HUNDRED AND " + self.trans_two(s[1:])
    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        if i < 0 or i >= len(self.NUMBER_MORE):
            raise ValueError("Index out of range")
        return self.NUMBER_MORE[i]