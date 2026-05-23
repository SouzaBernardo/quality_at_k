
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
        if string[center] == '|':
            return 1
        else:
            left = self.palindromic_length(center - diff, diff, string)
            right = self.palindromic_length(center + diff, diff, string)
            return max(left, right) + 1
    

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Create a new string with '|' characters added to both ends of the input string
        string = '|' + self.input_string + '|'
        # Initialize the palindromic length to 0 and the center to 0
        palindromic_length = 0
        center = 0
        # Iterate through all possible centers in the input string
        for i in range(1, len(string) - 1):
            # Calculate the difference between the current center and the current position
            diff = i - center
            # If the current position is within the palindromic substring, update the palindromic length
            if string[i] == string[center + diff]:
                palindromic_length = max(palindromic_length, 2 * diff + 1)
            # If the current position is outside the palindromic substring, expand the palindromic substring to include the current position
            else:
                left = self.palindromic_length(center - diff, diff, string)
                right = self.palindromic_length(center + diff, diff, string)
                palindromic_length = max(palindromic_length, left + right + 1)
            # Update the center of the palindromic substring to the current position
            center = i
        # Find the longest palindromic substring by iterating through all possible centers and selecting the one with the maximum length
        max_length = 0
        max_center = 0
        for i in range(1, len(string) - 1):
            diff = i - center
            left = self.palindromic_length(center - diff, diff, string)
            right = self.palindromic_length(center + diff, diff, string)
            length = left + right + 1
            if length > max_length:
                max_length = length
                max_center = i
        # Return the longest palindromic substring
        return self.input_string[max_center - max_length // 2:max_center + max_length // 2 + 1]