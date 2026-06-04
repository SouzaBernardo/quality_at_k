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
        """
        if center < 0 or center >= len(string):
            return 0
        if string[center] == '|':
            return self.palindromic_length(center - 1, diff, string) + 1
        if string[center] == '.':
            return self.palindromic_length(center - 1, diff, string) - 1
        if string[center] == '+':
            return self.palindromic_length(center - 1, diff, string) + diff

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        input_string = '|' + self.input_string + '|'
        max_length = 0
        max_center = 0
        for i in range(len(input_string)):
            length = self.palindromic_length(i, 1, input_string)
            if length > max_length:
                max_length = length
                max_center = i
        return self.input_string[max_center - max_length + 1:max_center + max_length]