class Manacher: 
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string





    def palindromic_string(self, center, diff, string):
        """
        Finds the longest palindromic substring in the given string.
        :param center: The center of the string, str.
        :param diff: The difference between the string and the center, str.
        :param string: The string itself, str.
        :return: The longest palindromic substring, str.
        """
        longest_palindromic_substring = ''
        for i in range(len(string)):
            if string[i] == center:
                longest_palindromic_substring = longest_palindromic_substring + diff[i]
                longest_palindromic_substring = max(longest_palindromic_substring, diff[i])
            else:
                longest_palindromic_substring = diff[i]
        return longest_palindromic_substring