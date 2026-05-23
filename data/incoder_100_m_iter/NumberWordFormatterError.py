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
        
        if x < 0:
            return "NEGATIVE"
        if x == 0:
            return "ZERO"
        if x > 0:
            words = self.NUMBER
            tens = x / 10
            units = x % 10
            if units == 0 and tens > 0:
                words = self.NUMBER_SUFFIX
            elif units == 0 and tens == 0:
                words = self.NUMBER_SUFFIX
            elif units > 0 and tens == 0:
                words = self.NUMBER_MORE
            elif units > 0 and tens > 0:
                words = self.NUMBER_TEEN
            elif units > 0 and tens == 0:
                words = self.NUMBER_TEEN
            elif units > 0 and tens > 0:
                words = self.NUMBER_TEN
            return " ".join(words[units:])
        else:
            return "NEGATIVE"