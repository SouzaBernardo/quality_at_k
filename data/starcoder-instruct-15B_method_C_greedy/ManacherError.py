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
        if diff < 0:
            return 0
        if center + diff >= len(string) or center - diff < 0:
            return 0
        if string[center + diff] == string[center - diff]:
            return 1 + 2 * self.palindromic_length(center, diff + 1, string)
        else:
            return max(self.palindromic_length(center, diff + 1, string), self.palindromic_length(center, diff - 1, string))


    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        max_length = 0
        max_substring = ''
        input_string = '$' + self.input_string + '&'
        for i in range(len(input_string)):
            left_length = self.palindromic_length(i, -1, input_string)
            right_length = self.palindromic_length(i, 1, input_string)
            current_length = left_length + right_length
            if current_length > max_length:
                max_length = current_length
                max_substring = input_string[i - left_length + 1: i + right_length]
        return max_substring[1:-1]