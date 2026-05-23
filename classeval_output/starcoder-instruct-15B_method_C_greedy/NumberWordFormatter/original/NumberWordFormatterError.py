
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
            return self.format_string(x)
        elif isinstance(x, float):
            return self.format_string(x)
        else:
            raise ValueError("Input must be int or float")


    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        integer_part = int(x)
        decimal_part = x - integer_part
        result = []

        if integer_part > 0:
            result.append(self.trans_three(str(integer_part)))

        if decimal_part > 0:
            result.append("POINT")
            result.append(self.trans_two(str(decimal_part)))

        return " ".join(result)

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        integer_part = int(s[0])
        decimal_part = int(s[1])

        integer_word = self.NUMBER[integer_part]
        decimal_word = self.NUMBER[decimal_part]

        if integer_part == 0:
            result = decimal_word
        elif integer_part == 1:
            result = self.NUMBER_TEEN[decimal_part - 1]
        elif integer_part > 1:
            result = integer_word + " " + self.NUMBER_TEN[decimal_part - 1]

        return result

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        integer_part = int(s[0])
        decimal_part = int(s[1:])

        result = ""
        if integer_part > 0:
            result += self.NUMBER[integer_part] + " "

        if decimal_part > 0:
            result += "AND " + self.trans_two(str(decimal_part))

        return result.strip()

    def parse_more(self, i):
        return self.NUMBER_MORE[i]