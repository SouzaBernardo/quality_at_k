
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
            return "0"
        if x == 1:
            return "1"
        if x == 2:
            return "2"
        if x == 3:
            return "3"
        if x == 4:
            return "4"
        if x == 5:
            return "5"
        if x == 6:
            return "6"
        if x == 7:
            return "7"
        if x == 8:
            return "8"
        if x == 9:
            return "9"
        if x == 10:
            return "10"
        if x == 11:
            return "11"
        if x == 12:
            return "12"
        if x == 13:
            return "13"
        if x == 14:
            return "14"
        if x == 15:
            return "15"
        if x == 16:
            return "16"
        if x == 17:
            return "17"
        if x == 18:
            return "18"
        if x == 19:
            return "19"
        if x == 20:
            return "20"
        if x == 21:
            return "21"
        if x == 22:
            return "22"
        if x == 23:
            return "23"
        if x == 24:
            return "24"
        if x == 25:
            return "25"
        if x == 26:
            return "26"
        if x == 27:
            return "27"
        if x == 28:
            return "28"
        if x == 29:
            return "29"
        if x == 30:
            return "30"
        if x == 31:
            return "31"
        if x == 32:
            return "32"
        if x == 33:
            return "33"
        if x == 34:
            return "34"
        if x == 35:
            return "35"
        if x == 36:
            return "36"
        if x == 37:
            return "37"
        if x == 38:
            return "38"
        if x == 39:
            return "39"
        if x == 40:
            return "40"
        if x == 41:
            return "41"
        if x == 42:
            return "42"
        if x == 43:
            return "43"
        if x == 44:
            return "44"
        if x == 45:
            return "45"
        if x == 46:
            return "46"
        if x == 47:
            return "47"
        if x == 48:
            return "48"
        if x == 49:
            return "49"
        if x == 50:
            return "50"
        if x == 51:
     







