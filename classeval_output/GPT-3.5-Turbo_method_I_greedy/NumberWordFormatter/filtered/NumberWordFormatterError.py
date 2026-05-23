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
        integer_part, decimal_part = divmod(x, 1)
        words = []
    
        # Convert integer part
        integer_part_str = str(int(integer_part))
        groups = [integer_part_str[max(i-3, 0):i] for i in range(len(integer_part_str), 0, -3)]
        groups.reverse()
        for group in groups:
            words.extend(self.convert_group(group))
    
        # Convert decimal part
        if decimal_part > 0:
            decimal_part_str = str(decimal_part)[2:]  # Remove "0." from decimal part
            for digit in decimal_part_str:
                words.append(self.convert_digit(digit))
    
        # Join words with "AND" and "ONLY"
        words_str = " ".join(words)
        words_str = words_str.replace(" AND ", " ")
        words_str += " ONLY"
    
        return words_str
    

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        number = float(x)
        return self.format(number)
    

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
            return self.NUMBER_TEN[tens_digit] + " " + self.NUMBER[ones_digit]
    

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        hundreds_digit = int(s[0])
        tens_digit = int(s[1])
        ones_digit = int(s[2])
    
        words = []
    
        # Convert hundreds digit
        if hundreds_digit > 0:
            words.append(self.NUMBER[hundreds_digit] + " HUNDRED")
    
        # Convert tens and ones digits
        if tens_digit == 1:
            words.append(self.NUMBER_TEEN[ones_digit])
        else:
            if tens_digit > 0:
                words.append(self.NUMBER_TEN[tens_digit])
            if ones_digit > 0:
                words.append(self.NUMBER[ones_digit])
    
        return " ".join(words)
    

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        return self.NUMBER_MORE[i]