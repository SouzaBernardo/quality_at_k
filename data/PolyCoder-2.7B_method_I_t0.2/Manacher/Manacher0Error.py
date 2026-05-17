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
        if center == 1:
            return string.count(center)
        if diff == 1:
            return string.count(center, diff)
        if center == 2:
            return string.count(center, diff, center)
        if diff == 2:
            return string.count(center, diff, center, diff)
        return self.palindromic_length(center - 1, diff - 1, string) + self.palindromic_length(center, diff - 1, string) + self.palindromic_length(center + 1, diff - 1, string)




    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        string = ''
        for i in range(len(self.input_string)):
            if self.input_string[i] == 'x':
                string += self.input_string[i]
            else:
                string += self.input_string[i]
        return string