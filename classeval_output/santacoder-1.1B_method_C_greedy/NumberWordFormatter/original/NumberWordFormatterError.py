
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
            return self.format_int(x)
        elif isinstance(x, float):
            return self.format_float(x)
        else:
            raise TypeError("NumberWordFormatter.format() expects an int or float, but got %s" % type(x))


    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if x == "":
            return ""
        if x == "0":
            return "ZERO"
        if x == "1":
            return "ONE"
        if x == "2":
            return "TWO"
        if x == "3":
            return "THREE"
        if x == "4":
            return "FOUR"
        if x == "5":
            return "FIVE"
        if x == "6":
            return "SIX"
        if x == "7":
            return "SEVEN"
        if x == "8":
            return "EIGHT"
        if x == "9":
            return "NINE"
        if x == "10":
            return "TEN"
        if x == "11":
            return "ELEVEN"
        if x == "12":
            return "TWELVE"
        if x == "13":
            return "THIRTEEN"
        if x == "14":
            return "FOURTEEN"
        if x == "15":
            return "FIFTEEN"
        if x == "16":
            return "SIXTEEN"
        if x == "17":
            return "SEVENTEEN"
        if x == "18":
            return "EIGHTEEN"
        if x == "19":
            return "NINETEEN"
        if x == "20":
            return "TWENTY"
        if x == "21":
            return "THIRTY"
        if x == "22":
            return "FORTY"
        if x == "23":
            return "FIFTY"
        if x == "24":
            return "SIXTY"
        if x == "25":
            return "SEVENTY"
        if x == "26":
            return "EIGHTY"
        if x == "27":
            return "NINETY"
        if x == "28":
            return "MILLION"
        if x == "29":
            return "BILLION"
        if x == "30":
            return "THOUSAND"
        if x == "31":
            return "HUNDRED"
        if x == "32":
            return "TEN"
        if x == "33":
            return "ELEVEN"
        if x == "34":
            return "TWELVE"
        if x == "35":
            return "THIRTEEN"
        if x == "36":
            return "FOURTEEN"
        if x == "37":
            return "FIFTEEN"
        if x == "38":
            return "SIXTEEN"
        if x == "39":
            return "SEVENTEEN"
        if x == "40":
            return "EIGHTEEN"
        if x == "41":
            return "NINETEEN"
        if x == "42":
            return "TWENTY"
        if x == "43":
            return "THIRTY"
        if x == "44":
            return "FORTY"
        if x == "45":
            return "FIFTY"
        if x == "46":
            return "SIXTY"
        if x == "47":
            return "SEVENTY"
        if x == "48":
            return "EIGHTY"
        if x == "49":
            return "NINETY"
        if x == "50":
            return "MILLION"
        if x == "51":
            return "HUNDRED"
        if x == "52":
            return "TEN"
        if x == "53":
            return "ELEVEN"
        if x == "54":
            return "TWELVE"
        if x == "55":
            return "THIRTEEN"
        if x == "56":
            return "FOURTEEN"
        if x == "57":
            return "FIFTEEN"
        if x == "58":
            return "SIXTEEN"
        if x == "59":
            return "SEVENTEEN"
        if x == "60":
            return "EIGHTEEN"
        if x == "61":
            return "NINETEEN"
        if x == "62":
            return "TWENTY"
        if x == "63":
            return "THIRTY"
        if x == "64":
            return "FORTY"
        if x == "65":
            return "FIFTY"
        if x == "66":
            return "SIXTY"
        if x == "67":
            return "SEVENTY"
        if x == "68":
            return "EIGHTY"
        if x == "69":
            return "NINETY"
        if x == "70":
            return "MILLION"
        if x == "71":
            return "HUNDRED"
        if x == "72":
            return "TEN"
        if x == "73":
            return "ELEVEN"
        if x == "74":
            return "TWELVE"
        if x == "75":
            return "THIRTEEN"
        if x == "76":
            return "FOURTEEN"
        if x == "77":
            return "FIFTEEN"
        if x == "78":
            return "SIXTEEN"
        if x == "79":
            return "SEVENTEEN"
        if x == "80":
            return "EIGHTEEN"
        if x == "81":
            return "NINETEEN"
        if x == "82":
            return "TWENTY"
        if x == "83":
            return "THIRTY"
        if x == "84":
            return "FORTY"
        if x == "85":
            return "FIFTY"
        if x == "86":
            return "SIXTY"
        if x == "87":
            return "SEVENTY"
        if x == "88":
            return "EIGHTY"
        if x == "89":
            return "NINETY"
        if x == "90":
            return "MILLION"
        if x == "91":
            return "HUNDRED"
        if x == "92":
            return "TEN"
        if x == "93":
            return "ELEVEN"
        if x == "94":
            return "TWELVE"
        if x == "95":
            return "THIRTEEN"
        if x == "96":
            return "FOURTEEN"
        if x == "97":
            return "FIFTEEN"
        if x == "98":
            return "SIXTEEN"
        if x == "99":
            return "SEVENTEEN"
        if x == "100":
            return "EIGHTEEN"
        if x == "101":
            return "NINETEEN"
        if x == "102":
            return "TWENTY"
        if x == "103":
            return "THIRTY"
        if x == "104":
            return "FORTY"
        if x == "105":
            return "FIFTY"
        if x == "106":
            return "SIXTY"
        if x == "107":
            return "SEVENTY"
        if x == "108":
           

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        if len(s) == 2:
            return self.NUMBER_TEEN[int(s)]
        else:
            return self.NUMBER_TEN[int(s[0])] + " " + self.NUMBER_MORE[int(s[1])]


    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        if len(s) == 3:
            return self.NUMBER[int(s)] + " HUNDRED AND " + self.NUMBER_MORE[int(s)]
        elif len(s) == 2:
            return self.NUMBER[int(s[0])] + " HUNDRED AND " + self.NUMBER_MORE[int(s[0])] + " " + self.NUMBER[int(s[1])]
        else:
            return self.NUMBER[int(s[0])] + " HUNDRED AND " + self.NUMBER_MORE[int(s[0])] + " " + self.NUMBER[int(s[1])] + " " + self.NUMBER[int(s[2])]


    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        if i == 1:
            return "THOUSAND"
        elif i == 2:
            return "MILLION"
        elif i == 3:
            return "BILLION"
        else:
            return ""
