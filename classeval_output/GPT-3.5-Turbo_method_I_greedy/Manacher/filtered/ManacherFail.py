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
        length = 0
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            length += 1
            diff += 1
        return length
    

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        string = self.input_string
        if len(string) < 2:
            return string
    
        # Preprocess the string to handle even-length palindromes
        processed_string = '#'.join('^{}$'.format(string))
    
        # Initialize variables
        center = 0
        diff = 0
        palindrome_lengths = [0] * len(processed_string)
        max_length = 0
        max_center = 0
    
        # Iterate through the processed string
        for i in range(1, len(processed_string) - 1):
            if i < diff:
                mirror = 2 * center - i
                palindrome_lengths[i] = min(diff - i, palindrome_lengths[mirror])
    
            # Expand around the current center
            while processed_string[i + 1 + palindrome_lengths[i]] == processed_string[i - 1 - palindrome_lengths[i]]:
                palindrome_lengths[i] += 1
    
            # Update the center and difference if the current palindrome extends beyond the previous one
            if i + palindrome_lengths[i] > diff:
                center = i
                diff = i + palindrome_lengths[i]
    
            # Update the maximum length and center if the current palindrome is longer
            if palindrome_lengths[i] > max_length:
                max_length = palindrome_lengths[i]
                max_center = i
    
        # Extract the longest palindromic substring from the processed string
        start = (max_center - max_length) // 2
        end = start + max_length
        longest_palindrome = string[start:end]
    
        return longest_palindrome