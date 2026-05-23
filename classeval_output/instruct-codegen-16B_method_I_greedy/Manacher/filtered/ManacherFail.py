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
        # Base case
        if diff == 0:
            return 1
        # If the characters at the current position and the center are not the same
            if string[center]!= string[diff]:
                return 1
        # Recursion
        else:
                return 1 + self.palindromic_length(center, diff - 1, string)

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Get the length of the input string
        n = len(self.input_string)
        # Create a new string with all the characters
        # in the input string
        new_string = '#' + '#'.join(self.input_string) + '#'
        # Create a list to store the palindromic substring
        palindromic_substring = [0] * n
        # Initialize the center of the palindromic substring
        center = 0
        # Calculate the longest palindromic substring
        for i in range(1, n):
            # Get the difference between the current position and the center
            diff = i - center
            # Check if the current position and the center are the same
            if new_string[i] == new_string[center]:
                # Update the palindromic substring
                palindromic_substring[i] = center - i + 1
                # Update the center of the palindromic substring
                if diff > 1:
                    center = i
                elif diff == 1:
                    center = i
                    palindromic_substring[i] = 1
                else:
                    palindromic_substring[i] = 0
            else:
                palindromic_substring[i] = 1
                if diff > 1:
                    center = i
                elif diff == 1:
                    center = i
                    palindromic_substring[i] = 1
                else:
                    palindromic_substring[i] = 0
        # Get the index of the longest palindromic substring
        max_length = 0
        max_index = 0
        for i in range(n):
            if palindromic_substring[i] > max_length:
                max_length = palindromic_substring[i]
                max_index = i
        # Return the longest palindromic substring
        return self.input_string[max_index - max_length + 1:max_index + max_length]