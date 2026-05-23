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
            return self.format_string(str(x)) + " ONLY"
        elif isinstance(x, float):
            integer_part, decimal_part = str(x).split('.')
            return self.format_string(integer_part) + " POINT " + self.format_string(decimal_part) + " ONLY"
        else:
            raise ValueError("Input must be an integer or a float")
    
    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        x = str(x)
        length = len(x)
        if length > 12:
            return "Number too large"
        x = x.zfill(12)
        res = []
        flag = False
        for i in range(0, 12, 3):
            temp = self.trans_three(x[i:i + 3])
            if temp:
                if flag:
                    res.append("AND")
                res.append(temp)
                res.append(self.NUMBER_MORE[3 - i // 3])
                flag = False
            elif i <= 9:
                flag = True
        return " ".join(res) + " ONLY"
    
    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        if len(s) == 1:
            return self.NUMBER[int(s)]
        elif s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]
        else:
            return self.NUMBER_TEN[int(s[0])-1] + " " + self.NUMBER[int(s[1])]
    
    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        s = s.zfill(3)
        if s[0] != "0":
            hundred_part = self.NUMBER[int(s[0])] + " HUNDRED"
        else:
            hundred_part = ""
        if s[1] != "0":
            if s[1] == "1":
                ten_part = self.NUMBER_TEEN[int(s[2])]
            else:
                ten_part = self.NUMBER_TEN[int(s[1])-1]
        else:
            ten_part = ""
        if s[2] != "0" and s[1] != "1":
            one_part = self.NUMBER[int(s[2])]
        else:
            one_part = ""
        if hundred_part and (ten_part or one_part):
            return hundred_part + " AND " + ten_part + " " + one_part
        else:
            return hundred_part + ten_part + one_part
    
    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        if i < len(self.NUMBER_MORE):
            return self.NUMBER_MORE[i]
        else:
            return "Index out of range"