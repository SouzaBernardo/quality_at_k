
class Manacher: 
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string



    def palindromic_length(self, center, diff, string):
        if string[center] == '|':
            return 1
        else:
            left_length = self.palindromic_length(center - diff, diff, string)
            right_length = self.palindromic_length(center + diff, diff, string)
            return left_length + right_length
    

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Create a new string with '#' added to the beginning and end of the input string.
        new_string = '#' + '#'.join(self.input_string) + '#'
        # Initialize variables for the center and the difference of the palindromes.
        center = 0
        diff = 0
        # Initialize a list to store the palindrome lengths.
        palindrome_lengths = []
        # Loop through the new string.
        for i in range(len(new_string)):
            # If the current character is a '#' and the next character is a '#',
            # then we have found a palindrome centered at i.
            if i < len(new_string) - 1 and new_string[i] == '#' and new_string[i+1] == '#':
                # Calculate the palindrome length and add it to the list.
                palindrome_length = self.palindromic_length(i, diff, new_string)
                palindrome_lengths.append(palindrome_length)
            # If the current character is a '#' and the next character is not a '#',
            # then we have found a palindrome centered at i with a smaller difference.
            elif i < len(new_string) - 1 and new_string[i] == '#' and new_string[i+1]!= '#':
                diff = i - center
                palindrome_lengths.append(1)
            # If the current character is not a '#' and the next character is a '#',
            # then we have found a palindrome centered at i with a larger difference.
            elif i < len(new_string) - 1 and new_string[i]!= '#' and new_string[i+1] == '#':
                diff = i - center
                palindrome_lengths.append(1)
            # If the current character is not a '#' and the next character is not a '#',
            # then we have found a palindrome centered at i with a difference of 0.
            elif i < len(new_string) - 1 and new_string[i]!= '#' and new_string[i+1]!= '#':
                diff = 0
                palindrome_lengths.append(1)
            # If the current character is a '#' and the next character is a '#',
            # then we have found a palindrome centered at i with a difference of 0.
            elif i == len(new_string) - 1 and new_string[i] == '#' and new_string[i-1] == '#':
                diff = 0
                palindrome_lengths.append(1)
            # If the current character is a '#' and the next character is not a '#',
            # then we have found a palindrome centered at i with a difference of 0.
            elif i == len(new_string) - 1 and new_string[i] == '#' and new_string[i-1]!= '#':
                diff = 0
                palindrome_lengths.append(1)
            # If the current character is not a '#' and the next character is a '#',
            # then we have found a palindrome centered at i with a difference of 0.
            elif i == len(new_string) - 1 and new_string[i]!= '#' and new_string[i-1] == '#':
                diff = 0
                palindrome_lengths.append(1)
            # If the current character is not a '#' and the next character is not a '#',
            # then we have found a palindrome centered at i with a difference of 0.
            elif i == len(new_string) - 1 and new_string[i]!= '#' and new_string[i-1]!= '#':
                diff = 0
                palindrome_lengths.append(1)
        # Find the maximum palindrome length.
        max_palindrome_length = max(palindrome_lengths)
        # Find the index of the maximum palindrome length in the list of palindrome lengths.
        max_palindrome_index = palindrome_lengths.index(max_palindrome_length)
        # Calculate the start and end indices of the longest palindromic substring.
        start_index = (max_palindrome_index - max_palindrome_length) // 2
        end_index = start_index + max_palindrome_length
        # Return the longest palindromic substring.
        return self.input_string[start_index:end_index]