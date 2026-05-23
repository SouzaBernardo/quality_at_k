class Manacher: 
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string



    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2

        """
        if center == 0:
            return diff
        if diff == 0:
            return 0
        if center == 1:
            return string.count(string[0])
        if center == 2:
            return string.count(string[1])
        if center == 3:
            return string.count(string[2])
        if center == 4:
            return string.count(string[3])
        if center == 5:
            return string.count(string[4])
        if center == 6:
            return string.count(string[5])
        if center == 7:
            return string.count(string[6])
        if center == 8:
            return string.count(string[7])
        if center == 9:
            return string.count(string[8])
        if center == 10:
            return string.count(string[9])
        if center == 11:
            return string.count(string[10])
        if center == 12:
            return string.count(string[11])
        if center == 13:
            return string.count(string[12])
        if center == 14:
            return string.count(string[13])
        if center == 15:
            return string.count(string[14])
        if center == 16:
            return string.count(string[15])
        if center == 17:
            return string.count(string[16])
        if center == 18:
            return string.count(string[17])
        if center == 19:
            return string.count(string[18])
        if center == 20:
            return string.count(string[19])
        if center == 21:
            return string.count(string[20])
        if center == 22:
            return string.count(string[21])
        if center == 23:
            return string.count(string[22])
        if center == 24:
            return string.count(string[23])
        if center == 25:
            return string.count(string[24])
        if center == 26:
            return string.count(string[25])
        if center == 27:
            return string.count(string[26])
        if center == 28:
            return string.count(string[27])
        if center == 29:
            return string.count(string[28])
        if center == 30:
            return string.count(string[29])
        if center == 31:
            return string.count(string[30])
        if center == 32:
            return string.count(string[31])
        if center == 33:
            return string.count(string[32])
        if center == 34:
            return string.count(string[33])
        if center == 35:
            return string.count(string[34])
        if center == 36:
            return string.count(string[35])
        if center == 37:
            return string.count(string[36])
        if center == 38:
            return string.count(string[37])
        if center == 39:
            return string.count(string[38])
        if center == 40:
            return string.count(string[39])
        if center == 41:
            return string.count(string[40])
        if center == 42:
            return string.count(string[41])
        if center == 43:
            return string.count(string[42])
        if center == 44:
            return string.count(string[43])
        if center == 45:
            return string.count(string[44])
        if center == 46:
            return string.count(string[45])
        if center == 47:
            return string.count(string[46])

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        return self.input_string[::-1]