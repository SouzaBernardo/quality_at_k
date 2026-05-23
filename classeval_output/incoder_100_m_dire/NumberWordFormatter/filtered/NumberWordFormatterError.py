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
            return "NEGATIVE"
        if x == 0:
            return "ZERO"
        if x > 0:
            words = self.format_string(x)
            words = words.split()
            words = [word for word in words if word != ""]
            words = [word for word in words if word != "and"]
            words = [word for word in words if word != "or"]
            words = [word for word in words if word != "but"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an"]
            words = [word for word in words if word != "the"]
            words = [word for word in words if word != "a"]
            words = [word for word in words if word != "an


    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        words = ""
        words = words + self.NUMBER[0]
        words = words + self.NUMBER_SUFFIX[0]
        words = words + self.NUMBER[1]
        words = words + self.NUMBER_SUFFIX[1]
        words = words + self.NUMBER[2]
        words = words + self.NUMBER_SUFFIX[2]
        words = words + self.NUMBER[3]
        words = words + self.NUMBER_SUFFIX[3]
        words = words + self.NUMBER[4]
        words = words + self.NUMBER_SUFFIX[4]
        words = words + self.NUMBER[5]
        words = words + self.NUMBER_SUFFIX[5]
        words = words + self.NUMBER[6]
        words = words + self.NUMBER_SUFFIX[6]
        words = words + self.NUMBER[7]
        words = words + self.NUMBER_SUFFIX[7]
        words = words + self.NUMBER[8]
        words = words + self.NUMBER_SUFFIX[8]
        words = words + self.NUMBER[9]
        words = words + self.NUMBER_SUFFIX[9]
        words = words + self.NUMBER[10]
        words = words + self.NUMBER_SUFFIX[10]
        words = words + self.NUMBER[11]
        words = words + self.NUMBER_SUFFIX[11]
        words = words + self.NUMBER[12]
        words = words + self.NUMBER_SUFFIX[12]
        words = words + self.NUMBER[13]
        words = words + self.NUMBER_SUFFIX[13]
        words = words + self.NUMBER[14]
        words = words + self.NUMBER_SUFFIX[14]
        words = words + self.NUMBER[15]
        words = words + self.NUMBER_SUFFIX[15]
        words = words + self.NUMBER[16]
        words = words + self.NUMBER_SUFFIX[16]
        words = words + self.NUMBER[17]
        words = words + self.NUMBER_SUFFIX[17]
        words = words + self.NUMBER[18]
        words = words + self.NUMBER_SUFFIX[18]
        words = words + self.NUMBER[19]
        words = words + self.NUMBER_SUFFIX[19]
        words = words + self.NUMBER[20]
        words = words + self.NUMBER_SUFFIX[20]
        words = words + self.NUMBER[21]
        words = words + self.NUMBER_SUFFIX[21]
        words = words + self.NUMBER[22]
        words = words + self.NUMBER_SUFFIX[22]
        words = words + self.NUMBER[23]
        words = words + self.NUMBER_SUFFIX[23]
        words = words + self.NUMBER[24]
        words = words + self.NUMBER_SUFFIX[24]
        words = words + self.NUMBER[25]
        words = words + self.NUMBER_SUFFIX[25]
        words = words + self.NUMBER[26]
        words = words + self.NUMBER_SUFFIX[26]
        words = words + self.NUMBER[27]
        words = words + self.NUMBER_SUFFIX[27]
        words = words + self.NUMBER[28]
        words = words + self.NUMBER_SUFFIX[28]
        words = words + self.NUMBER[29]
        words = words + self.NUMBER_SUFFIX[29]
        words = words + self.NUMBER[30]
        words = words + self.NUMBER_SUFFIX[30]
        words = words + self.NUMBER[31]
        words = words + self.NUMBER_SUFFIX[31]
        words = words + self.NUMBER[32]
        words = words + self.NUMBER_SUFFIX[32]
        words = words + self.NUMBER[33]
        words = words + self.NUMBER_SUFFIX[33]
        words = words + self.NUMBER[34]
        words = words + self.NUMBER_SUFFIX[34]
        words = words + self.NUMBER[35]
        words = words + self.NUMBER_SUFFIX[35]
        words = words + self.NUMBER[36]
        words = words + self.NUMBER_SUFFIX[36]
        words = words + self.NUMBER[37]
        words = words + self.NUMBER_SUFFIX[37]
        words = words + self.NUMBER[38]
        words = words + self.NUMBER_SUFFIX[38]
        words = words + self.NUMBER[39]
        words = words + self.NUMBER_SUFFIX[39]
        words = words + self.NUMBER[40]
        words = words + self.NUMBER_SUFFIX[40]
        words = words + self.NUMBER[41]
        words = words + self.NUMBER_SUFFIX[41]
        words = words + self.NUMBER[42]
        words = words + self.NUMBER_SUFFIX[42]
        words = words + self.NUMBER[43]
        words = words + self.NUMBER_SUFFIX[43]
        words = words + self.NUMBER[44]
        words = words + self.NUMBER_SUFFIX[44]
        words = words + self.NUMBER[45]
        words = words + self.NUMBER_SUFFIX[45]
        words = words + self.NUMBER[46]
        words = words + self.NUMBER_SUFFIX[46]
        words = words + self.NUMBER[47]
        words = words + self.NUMBER_SUFFIX[47]
        words = words + self.NUMBER[48]
        words = words + self.NUMBER_SUFFIX[48]
        words = words + self.NUMBER[49]
        words = words + self.NUMBER_SUFFIX[49]
        words = words + self.NUMBER[50]
        words = words + self.NUMBER_SUFFIX[50]
        words = words + self.NUMBER[51]
        words = words + self.NUMBER_SUFFIX[51]
        words = words + self.NUMBER[52]
        words = words + self.NUMBER_SUFFIX[52]
        words = words + self.NUMBER[53]
        words = words + self.NUMBER_SUFFIX[53]
        words = words + self.NUMBER[54]
        words = words + self.NUMBER_SUFFIX[54]
        words = words + self.NUMBER[55]
        words = words + self.NUMBER_SUFFIX[55]
        words = words + self.NUMBER[56]
        words = words + self.NUMBER_SUFFIX[56]
        words = words + self.NUMBER[57]
        words = words + self.NUMBER_SUFFIX[57]
        words = words + self.NUMBER[58]
        words = words + self.NUMBER_SUFFIX[58]
        words = words + self.NUMBER[59]
        words = words + self.NUMBER_SUFFIX[59]
        words = words + self.NUMBER[60]
        words = words + self.NUMBER_SUFFIX[60]
        words = words + self.NUMBER[61]
        words = words + self.NUMBER_SUFFIX[61]
        words = words + self.NUMBER[62]
        words = words + self.NUMBER_SUFFIX[62]
        words = words + self.NUMBER[63]
        words = words + self.NUMBER_SUFFIX[63]
        words = words + self.NUMBER[64]
        words = words + self.NUMBER_SUFFIX[64]
        words = words + self.NUMBER[65]
        words = words + self.NUMBER_SUFFIX[65]
        words = words + self.NUMBER[66]
        words = words + self.NUMBER_SUFFIX[66]
        words = words + self.NUMBER[67]
        words = words + self.NUMBER_SUFFIX[67]
        words = words + self.NUMBER[68]
        words = words + self.NUMBER_SUFFIX[68]
        words = words + self.NUMBER[69]
        words = words + self.NUMBER_SUFFIX[69]
        words = words + self.NUMBER[70]
        words = words + self.NUMBER_SUFFIX[70]
        words = words + self.NUMBER[71]
        words = words + self.NUMBER_SUFFIX[71]
        words = words + self.NUMBER[72]
        words = words + self.NUMBER_SUFFIX[72]
        words = words + self.NUMBER[73]
        words = words + self.NUMBER_SUFFIX[73]
        words = words + self.NUMBER[74]
        words = words + self.NUMBER_SUFFIX[74]
        words = words + self.NUMBER[75]
        words = words + self.NUMBER_SUFFIX[75]
        words = words + self.NUMBER[76]
        words = words + self.NUMBER_SUFFIX[76]
        words = words + self.NUMBER[77]
        words = words + self.NUMBER_SUFFIX[77]
        words = words + self.NUMBER[78]
        words = words + self.NUMBER_SUFFIX[78]
        words = words + self.NUMBER[79]



    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        words = self.NUMBER
        if int(s) < 20:
            words = self.NUMBER_SUFFIX
        elif int(s) < 100:
            words = self.NUMBER_MORE
        elif int(s) < 1000:
            words = self.NUMBER_TEEN
        elif int(s) < 10000:
            words = self.NUMBER_TEN
        return words[int(s)-1]


    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        words = []
        words.append(self.NUMBER[int(x) % 100])
        words.append(self.NUMBER[int(x) % 10])
        words.append(self.NUMBER[int(x) % 10])
        return " ".join(words)


    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        magnitude = i
        if magnitude == 0:
            return ""
        elif magnitude == 1:
            return self.NUMBER_SUFFIX[0]
        elif magnitude == 2:
            return self.NUMBER_SUFFIX[1]
        elif magnitude == 3:
            return self.NUMBER_SUFFIX[2]
        elif magnitude == 4:
            return self.NUMBER_SUFFIX[3]
        elif magnitude == 5:
            return self.NUMBER_SUFFIX[4]
        elif magnitude == 6:
            return self.NUMBER_SUFFIX[5]
        elif magnitude == 7:
            return self.NUMBER_SUFFIX[6]
        elif magnitude == 8:
            return self.NUMBER_SUFFIX[7]
        elif magnitude == 9:
            return self.NUMBER_SUFFIX[8]
        elif magnitude == 10:
            return self.NUMBER_SUFFIX[9]
        elif magnitude == 11:
            return self.NUMBER_SUFFIX[10]
        elif magnitude == 12:
            return self.NUMBER_SUFFIX[11]
        elif magnitude == 13:
            return self.NUMBER_SUFFIX[12]
        elif magnitude == 14:
            return self.NUMBER_SUFFIX[13]
        elif magnitude == 15:
            return self.NUMBER_SUFFIX[14]
        elif magnitude == 16:
            return self.NUMBER_SUFFIX[15]
        elif magnitude == 17:
            return self.NUMBER_SUFFIX[16]
        elif magnitude == 18:
            return self.NUMBER_SUFFIX[17]
        elif magnitude == 19:
            return self.NUMBER_SUFFIX[18]
        elif magnitude == 20:
            return self.NUMBER_SUFFIX[19]
        elif magnitude == 21:
            return self.NUMBER_SUFFIX[20]
        elif magnitude == 22:
            return self.NUMBER_SUFFIX[21]
        elif magnitude == 23:
            return self.NUMBER_SUFFIX[22]
        elif magnitude == 24:
            return self.NUMBER_SUFFIX[23]
        elif magnitude == 25:
            return self.NUMBER_SUFFIX[24]
        elif magnitude == 26:
            return self.NUMBER_SUFFIX[25]
        elif magnitude == 27:
            return self.NUMBER_SUFFIX[26]
        elif magnitude == 28:
            return self.NUMBER_SUFFIX[27]
        elif magnitude == 29:
            return self.NUMBER_SUFFIX[28]
        elif magnitude == 30:
            return self.NUMBER_SUFFIX[29]
        elif magnitude == 31:
            return self.NUMBER_SUFFIX[30]
        elif magnitude == 32:
            return self.NUMBER_SUFFIX[31]
        elif magnitude == 33:
            return self.NUMBER_SUFFIX[32]
        elif magnitude == 34:
            return self.NUMBER_SUFFIX[33]
        elif magnitude == 35:
            return self.NUMBER_SUFFIX[34]
        elif magnitude == 36:
            return self.NUMBER_SUFFIX[35]
        elif magnitude == 37:
            return self.NUMBER_SUFFIX[36]
        elif magnitude == 38:
            return self.NUMBER_SUFFIX[37]
        elif magnitude == 39:
            return self.NUMBER_SUFFIX[38]
        elif magnitude == 40:
            return self.NUMBER_SUFFIX[39]
        elif magnitude == 41:
            return self.NUMBER_SUFFIX[40]
        elif magnitude == 42:
            return self.NUMBER_SUFFIX[41]
        elif magnitude == 43:
            return self.NUMBER_SUFFIX[42]
        elif magnitude == 44:
            return self.NUMBER_SUFFIX[43]
        elif magnitude == 45:
            return self.NUMBER_SUFFIX[44]
        elif magnitude == 46:
            return self.NUMBER_SUFFIX[45]
        elif magnitude == 47:
            return self.NUMBER_SUFFIX[46]
        elif magnitude == 48:
            return self.NUMBER_SUFFIX[47]
        elif magnitude == 49:
            return self.NUMBER_SUFFIX[48]
        elif magnitude == 50:
            return self.NUMBER_SUFFIX[49]
        elif magnitude == 51:
            return self.NUMBER_SUFFIX[50]
        elif magnitude == 52:
            return self.NUMBER_SUFFIX[51]
        elif magnitude == 53:
            return self.NUMBER_SUFFIX[52]
        elif magnitude == 54:
            return self.NUMBER_SUFFIX[53]
        elif magnitude == 55:
            return self.NUMBER_SUFFIX[54]
        elif magnitude == 56:
            return self.NUMBER_SUFFIX[55]
        elif magnitude == 57:
            return self.NUMBER_SUFFIX[56]
        elif magnitude == 58:
            return self.NUMBER_SUFFIX[57]
        elif magnitude == 59:
            return self.NUMBER_SUFFIX[58]
        elif magnitude == 60:
            return self.NUMBER_SUFFIX[59]
        elif magnitude == 61:
            return self.NUMBER_SUFFIX[60]
        elif magnitude == 62:
            return self.NUMBER_SUFFIX[61]
        elif magnitude == 63:
            return self.NUMBER_SUFFIX[62]
        elif magnitude == 64:
            return self.NUMBER_SUFFIX[63]
        elif magnitude == 65:
            return self.NUMBER_SUFFIX[64]
        elif magnitude == 66:
            return self.NUMBER_SUFFIX[65]
        elif magnitude == 67:
            return self.NUMBER_SUFFIX[66]
        elif magnitude == 68:
            return self.NUMBER_SUFFIX[67]
        elif magnitude == 69:
            return self.NUMBER_SUFFIX[68]
        elif magnitude == 70:
            return self.NUMBER_SUFFIX[69]
        elif magnitude == 71:
            return self.NUMBER_SUFFIX[70]
        elif magnitude == 72:
            return self.NUMBER_SUFFIX[71]
        elif magnitude == 73:
            return self.NUMBER_SUFFIX[72]
        elif magnitude == 74:
            return self.NUMBER_SUFFIX[73]
        elif magnitude == 75:
            return self.NUMBER_SUFFIX[74]
        elif magnitude == 76:
            return self.NUMBER_SUFFIX[75]
        elif magnitude == 77:
            return self.NUMBER_SUFFIX[76]
        elif magnitude == 78:
            return self.NUMBER_SUFFIX[77]
        elif magnitude == 79:
            return self.NUMBER_SUFFIX[78]
        elif magnitude == 80:
            return self.NUMBER_SUFFIX[79]
        elif magnitude == 81:
            return self.NUMBER_SUFFIX[80]
        elif magnitude == 82:
            return self.NUMBER_SUFFIX[81]
        elif magnitude == 83:
            return self.NUMBER_SUFFIX[82]
        elif magnitude == 84:
            return self.NUMBER_SUFFIX[83]
        elif magnitude == 85:
            return self.NUMBER_SUFFIX[84]
        elif magnitude == 86:
            return self.NUMBER_SUFFIX[85]
        elif magnitude == 87:
            return self.NUMBER_SUFFIX[86]
        elif magnitude == 88:
            return self.NUMBER_SUFFIX[87]
        elif magnitude == 89:
            return self.NUMBER_SUFFIX[88]
        elif magnitude == 90:
            return self.NUMBER_SUFFIX[89]
        elif magnitude == 91:
            return self.NUMBER_SUFFIX[90]
        elif magnitude == 92:
            return self.NUMBER_SUFFIX[91]
        elif magnitude == 93:
            return self.NUMBER_SUFFIX[92]
        elif magnitude == 94:
            return self.NUMBER_SUFFIX[93]
        elif magnitude == 95:
            return self.NUMBER_SUFFIX[94]
        elif magnitude == 96:
            return self.NUMBER_SUFFIX[95]
        elif magnitude == 97:
            return self.NUMBER_SUFFIX[96]
        elif magnitude == 98:
            return self.NUMBER_SUFFIX[97]
        elif magnitude == 99:
            return self.NUMBER_SUFFIX[98]
        elif magnitude == 100:
            return self.NUMBER_SUFFIX[99]
        elif magnitude == 101:
            return self.NUMBER_SUFFIX[100]
        elif magnitude == 102:
            return self.NUMBER_SUFFIX[101]
        elif magnitude == 103:
            return self.NUMBER_SUFFIX[102]
        elif magnitude == 104:
            return self.NUMBER_SUFFIX[103]
        elif magnitude == 105:
            return self.NUMBER_SUFFIX[104]
        elif magnitude == 106:
            return self.NUMBER_SUFFIX[105]
        elif magnitude == 107:
            return self.NUMBER_SUFFIX[106]
        elif magnitude == 108:
            return self.NUMBER_SUFFIX[107]
        elif magnitude == 109:
            return self.NUMBER_SUFFIX[108]
        elif magnitude == 110:
            return self.NUMBER_SUFFIX[109]
        elif magnitude == 111:
            return self.NUMBER_SUFFIX[110]
        elif magnitude == 112:
            return self.NUMBER_SUFFIX[111]
        elif magnitude == 113:
            return self.NUMBER_SUFFIX[112]
        elif magnitude == 114:
            return self.NUMBER_SUFFIX[113]
        elif magnitude == 115:
            return self.NUMBER_SUFFIX[114]
        elif magnitude == 116:
            return self.NUMBER_SUFFIX[115]
        elif magnitude == 117:
            return self.NUMBER_SUFFIX[116]
        else:
            return ""