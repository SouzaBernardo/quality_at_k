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
        if diff == 0:
            return 1
        elif diff == 1:
            if string[center] == string[center - 1]:
                return self.palindromic_length(center - 1, diff - 1, string) + 1
            else:
                return 0
        else:
            return max(self.palindromic_length(center - 1, diff - 1, string), self.palindromic_length(center + 1, diff - 1, string))




    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        if len(self.input_string) == 0:
            return ''
        else:
            center = 0
            diff = 1
            string = self.input_string
            while diff < len(string):
                length = self.palindromic_length(center, diff, string)
                if length > len(string):
                    diff = length
                else:
                    center = center + length - 1
                    diff = diff + 1
            return string[center - diff:center + diff]