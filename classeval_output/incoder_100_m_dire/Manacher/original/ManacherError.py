
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
        center = center + diff
        if center >= len(string):
            return 1
        if string[center] == string[center - diff]:
            return self.palindromic_length(center, diff, string)
        else:
            return 1 + self.palindromic_length(center, diff, string)



    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        center = len(self.input_string) // 2
        diff = 1
        string = center
        while diff != 0 and string != 1:
            diff = 0
            string = self.palindromic_length(center, diff, self.input_string)
            center += diff
        return string

