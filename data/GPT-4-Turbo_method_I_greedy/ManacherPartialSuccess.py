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
        if center - diff < 0 or center + diff >= len(string) or string[center - diff] != string[center + diff]:
            return diff - 1
        return self.palindromic_length(center, diff + 1, string)
    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        string = '#' + '#'.join(self.input_string) + '#'
        right, center = 0, 0
        length = [0] * len(string)
        max_length, max_length_center = 0, 0
    
        for i in range(len(string)):
            if i < right:
                length[i] = min(right - i, length[2 * center - i])
            length[i] = self.palindromic_length(i, length[i] + 1, string)
            if i + length[i] > right:
                center, right = i, i + length[i]
            if length[i] > max_length:
                max_length, max_length_center = length[i], i
    
        start = (max_length_center - max_length) // 2
        end = start + max_length
        return self.input_string[start:end]