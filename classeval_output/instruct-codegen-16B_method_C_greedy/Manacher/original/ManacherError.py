
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
        """
        if diff == 0:
            return 1
        if diff == 1:
            if string[center] == string[center - 1]:
                return 2
            else:
                return 1
        if diff > 1:
            if string[center] == string[center - diff]:
                return diff + 1
            else:
                return 1 + min(self.palindromic_length(center + 1, diff - 1, string),
                self.palindromic_length(center, diff - 1, string),
                self.palindromic_length(center - diff, diff - 1, string))

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Initialize the variables
        max_length = 1
        max_length_center = 0
        max_length_diff = 0
        # Run the algorithm on each character of the input_string
        for i in range(len(self.input_string)):
            # Find the longest palindromic substring
            current_length = 1
            current_length_center = i
            current_length_diff = 0
            # Check whether the character is part of a palindrome
            while (i - current_length_center >= 0 and
                i + current_length_center < len(self.input_string)):
                if (self.input_string[i - current_length_center] ==
                self.input_string[i + current_length_center]):
                    current_length += 1
                    current_length_center = i
                    current_length_diff = 0
                else:
                    if (current_length > max_length):
                        max_length = current_length
                        max_length_center = current_length_center
                        max_length_diff = current_length_diff
                    break
            # Check whether the character is part of a palindrome
            while (i - current_length_center >= 0 and
                i + current_length_center + 1 < len(self.input_string)):
                if (self.input_string[i - current_length_center] ==
                self.input_string[i + current_length_center + 1]):
                    current_length += 1
                    current_length_center = i
                    current_length_diff = 0
                else:
                    if (current_length > max_length):
                        max_length = current_length
                        max_length_center = current_length_center
                        max_length_diff = current_length_diff
                    break
            # Update the current length and center
            if (current_length > max_length):
                max_length = current_length
                max_length_center = current_length_center
                max_length_diff = current_length_diff
        # Return the result
        return self.input_string[max_length_center - max_length + 1:max_length_center + max_length]