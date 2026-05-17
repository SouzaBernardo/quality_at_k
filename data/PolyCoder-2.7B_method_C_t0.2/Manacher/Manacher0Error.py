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
        else:
            return self.palindromic_length(center - 1, diff, string) + self.palindromic_length(center, diff, string)




    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        string = self.input_string
        length = len(string)
        if length == 0:
            return ''
        if length == 1:
            return string

        if length == 2:
            if string[0] == string[1]:
                return string
            else:
                return string[1:]

        if length == 3:
            if string[0] == string[1] and string[2] == string[3]:
                return string
            else:
                return string[1:]

        if length == 4:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5]:
                return string
            else:
                return string[1:]

        if length == 5:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7]:
                return string
            else:
                return string[1:]

        if length == 6:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9]:
                return string
            else:
                return string[1:]

        if length == 7:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11]:
                return string
            else:
                return string[1:]

        if length == 8:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11] and string[12] == string[13]:
                return string
            else:
                return string[1:]

        if length == 9:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11] and string[12] == string[13] and string[14] == string[15]:
                return string
            else:
                return string[1:]

        if length == 10:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11] and string[12] == string[13] and string[14] == string[15] and string[16] == string[17]:
                return string
            else:
                return string[1:]

        if length == 11:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11] and string[12] == string[13] and string[14] == string[15] and string[16] == string[17] and string[18] == string[19]:
                return string
            else:
                return string[1:]

        if length == 12:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11] and string[12] == string[13] and string[14] == string[15] and string[16] == string[17] and string[18] == string[19] and string[20] == string[21]:
                return string
            else:
                return string[1:]

        if length == 13:
            if string[0] == string[1] and string[2] == string[3] and string[4] == string[5] and string[6] == string[7] and string[8] == string[9] and string[10] == string[11] and string[12] == string[13] and string[14] == string[15] and string[16] == string[17] and string[18] == string[19] and string[20] == string[21]