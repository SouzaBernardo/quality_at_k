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
        length = 0
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            length += 1
            diff += 1
        return length
    

    def palindromic_string(self):
        max_length = 0
        start_index = 0
    
        for i in range(len(self.input_string)):
            length = self.palindromic_length(i, 0, self.input_string)
            if length > max_length:
                max_length = length
                start_index = i - length // 2
    
        return self.input_string[start_index:start_index + max_length]