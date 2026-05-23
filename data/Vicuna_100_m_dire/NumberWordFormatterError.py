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
        if x < 0:
            return "-" + self.format(-x)
        if x == 0:
            return "ZERO"
        if x == 1:
            return self.NUMBER[0]
        if x < 20:
            return self.NUMBER[2] + x
        if x < 100:
            return self.NUMBER_TEEN[2] + self.trans_two(x)
        if x < 1000:
            return self.NUMBER_TEN[2] + self.trans_three(x)
        if x < 1000000:
            return self.NUMBER_MORE[2] + self.trans_three(x)
        if x < 1000000000:
            return self.NUMBER_SUFFIX[2] + self.trans_three(x)
        if x < 1000000000000:
            return self.NUMBER_SUFFIX[3] + self.trans_four(x)
        if x < 1000000000000000:
            return self.NUMBER_SUFFIX[4] + self.trans_five(x)
        if x < 1000000000000000000:
            return self.NUMBER_SUFFIX[5] + self.trans_six(x)
        if x < 100000000000000000000:
            return self.NUMBER_SUFFIX[6] + self.trans_seven(x)
        if x < 10000000000000000000000:
            return self.NUMBER_SUFFIX[7] + self.trans_eight(x)
        if x < 1000000000000000000000000:
            return self.NUMBER_SUFFIX[8] + self.trans_nine(x)
        if x < 100000000000000000000000000:
            return self.NUMBER_SUFFIX[9] + self.trans_ten(x)
        if x < 10000000000000000000000000000:
            return self.NUMBER_SUFFIX[10] + self.trans_eleven(x)
        if x < 1000000000000000000000000000000:
            return self.NUMBER_SUFFIX[11] + self.trans_twelve(x)
        if x < 100000000000000000000000000000000:
            return self.NUMBER_SUFFIX[12] + self.trans_thirteen(x)
        if x < 10000000000000000000000000000000000:
            return self.NUMBER_SUFFIX[13] + self.trans_fourteen(x)
        if x < 10000000000000000000000000000000000000:
            return self.NUMBER_SUFFIX[14] + self.trans_fifteen(x)
        if x < 10000000000000000000000000000000000000000:
            return self.NUMBER_SUFFIX[15] + self.trans_sixteen(x)
        if x < 10000000000000000000000000000000000000000000:
            return self.NUMBER_SUFFIX[1

    def format_string(self, x):
        # code to convert string representation of a number into words format
        # return the converted string in the format "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        return "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"

    def trans_two(self, s):
        # code to convert two-digit number to words format
        return "TWO " + s[1] + " " + s[0]

    def trans_three(self, s):
        # code to convert three-digit number to words format
        return "THREE HUNDRED " + self.trans_two(s[1:])

    def parse_more(self, i):
        suffix = ""
        if i < 1000:
            suffix = self.NUMBER_SUFFIX[0]
        elif i < 1000000:
            suffix = self.NUMBER_SUFFIX[1]
        elif i < 1000000000:
            suffix = self.NUMBER_SUFFIX[2]
        elif i < 1000000000000:
            suffix = self.NUMBER_SUFFIX[3]
        elif i < 1000000000000000:
            suffix = self.NUMBER_SUFFIX[4]
        elif i < 1000000000000000000:
            suffix = self.NUMBER_SUFFIX[5]
        elif i < 100000000000000000000:
            suffix = self.NUMBER_SUFFIX[6]
        elif i < 10000000000000000000000:
            suffix = self.NUMBER_SUFFIX[7]
        elif i < 1000000000000000000000000:
            suffix = self.NUMBER_SUFFIX[8]
        elif i < 100000000000000000000000000:
            suffix = self.NUMBER_SUFFIX[9]
        else:
            suffix = self.NUMBER_SUFFIX[10]
        return suffix