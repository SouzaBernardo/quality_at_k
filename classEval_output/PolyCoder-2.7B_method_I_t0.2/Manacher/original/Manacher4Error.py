
class Manacher:  
    """
    his is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

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
        if string == '':
            return 0
        if center == 1:
            return self.palindromic_length(string[0], diff-1, string[1:])
        if center == 2:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:])
        if center == 3:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:])
        if center == 4:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:])
        if center == 5:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:])
        if center == 6:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:]) + self.palindromic_length(string[5], diff-1, string[6:])
        if center == 7:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:]) + self.palindromic_length(string[5], diff-1, string[6:]) + self.palindromic_length(string[6], diff-1, string[7:])
        if center == 8:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:]) + self.palindromic_length(string[5], diff-1, string[6:]) + self.palindromic_length(string[6], diff-1, string[7:]) + self.palindromic_length(string[7], diff-1, string[8:])
        if center == 9:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:]) + self.palindromic_length(string[5], diff-1, string[6:]) + self.palindromic_length(string[6], diff-1, string[7:]) + self.palindromic_length(string[7], diff-1, string[8:]) + self.palindromic_length(string[8], diff-1, string[9:])
        if center == 10:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:]) + self.palindromic_length(string[5], diff-1, string[6:]) + self.palindromic_length(string[6], diff-1, string[7:]) + self.palindromic_length(string[7], diff-1, string[8:]) + self.palindromic_length(string[8], diff-1, string[9:]) + self.palindromic_length(string[9], diff-1, string[10:])
        if center == 11:
            return self.palindromic_length(string[0], diff-1, string[1:]) + self.palindromic_length(string[1], diff-1, string[2:]) + self.palindromic_length(string[2], diff-1, string[3:]) + self.palindromic_length(string[3], diff-1, string[4:]) + self.palindromic_length(string[4], diff-1, string[5:]) + self.

