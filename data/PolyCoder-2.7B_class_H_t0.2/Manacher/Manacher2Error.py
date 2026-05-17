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

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """

    def palindromic_string_with_center(self, center):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_center(2)
        'ababaxse'

        """

    def palindromic_string_with_diff(self, center, diff):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_diff(2, 1)
        'ababa'

        """

    def palindromic_string_with_center_and_diff(self, center, diff):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_center_and_diff(2, 1)
        'ababaxse'

        """

    def palindromic_string_with_diff_and_center(self, center, diff):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_diff_and_center(2, 1)
        'ababaxse'

        """

    def palindromic_string_with_center_and_diff_and_center(self, center, diff, center):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param center: The center of the palindromic substring, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_center_and_diff_and_center(2, 1, 2)
        'ababaxse'

        """

    def palindromic_string_with_diff_and_center(self, center, diff, center):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param center: The center of the palindromic substring, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_diff_and_center(2, 1, 2)
        'ababaxse'

        """

    def palindromic_string_with_center_and_diff_and_center(self, center, diff, center):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param center: The center of the palindromic substring, int.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string_with_center_and_diff_and_center(2, 1, 2)
        'ababaxse'

        """

    def palindromic_string_with_diff_and_center(self, center, diff, center):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.