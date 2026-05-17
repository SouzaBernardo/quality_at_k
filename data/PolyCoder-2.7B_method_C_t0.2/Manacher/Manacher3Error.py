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
        if center == 0:
            return diff
        else:
            return self.palindromic_length(center - 1, diff, string)




    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        string = self.input_string
        length = len(string)
        if length == 0:
            return ''
        
        if length == 1:
            return string
        
        if length == 2:
            return string[0] + string[1]
        
        if length == 3:
            return string[0] + string[1] + string[2]
        
        if length == 4:
            return string[0] + string[1] + string[2] + string[3]
        
        if length == 5:
            return string[0] + string[1] + string[2] + string[3] + string[4]
        
        if length == 6:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5]
        
        if length == 7:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6]
        
        if length == 8:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7]
        
        if length == 9:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8]
        
        if length == 10:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9]
        
        if length == 11:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10]
        
        if length == 12:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11]
        
        if length == 13:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12]
        
        if length == 14:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13]
        
        if length == 15:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14]
        
        if length == 16:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15]
        
        if length == 17:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15] + string[16]
        
        if length == 18:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15] + string[16] + string[17]
        
        if length == 19:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15] + string[16] + string[17] + string[18]
        
        if length == 20:
            return string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15] + string[16]