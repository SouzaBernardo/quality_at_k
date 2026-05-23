class BoyerMooreSearch: 
    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        """
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)



    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        >>> boyer Moore Search = Boyer Moore Search("ABAABA", "AB")
        >>> boyer Moore Search.match_in_pattern("A")
        0

        """
        # Check if the character is in the pattern
        if char in self.pattern:
            # Get the index of the character in the pattern
            index = self.pattern.index(char)
            # Check if the index is the rightmost index
            if index < self.textLen - 1:
                return index
        # If the character is not in the pattern, return -1
        else:
            return -1



    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        pattern = self.pattern.lower() # convert the pattern to lowercase
        text = self.text.lower() # convert the text to lowercase
        pattern_list = []
        for i in range(self.textLen):
            char = self.text[i]
            currentPos = i
            if char.isalnum() and pattern == pattern_list:
                # if the character is a digit and the pattern is in the list,
                # it means that the position is the first position in the list
                if currentPos == 0:
                    pattern_list.append(currentPos)
                else:
                    # check if the character is the first character in the pattern
                    if pattern[0] == char:
                        # if the character is the first character in the pattern,
                        # it means that the position is the first position in the list
                        pattern_list.append(currentPos)
                    else:
                        # check if the character is the second character in the pattern
                        if pattern[0] == pattern[1]:
                            # if the character is the second character in the pattern,
                            # it means that the position is the second position in the list
                            pattern_list.append(currentPos)
                        else:
                            # check if the character is the third character in the pattern
                            if pattern[0] == pattern[2]:
                                # if the character is the third character in the pattern,
                                # it means that the position is the third position in the list
                                pattern_list.append(currentPos)
                            else:
                                # check if the character is the fourth character in the pattern
                                if pattern[0] == pattern[3]:
                                    # if the character is the fourth character in the pattern,
                                    # it means that the position is the fourth position in the list
                                    pattern_list.append(currentPos)
                                else:
                                    # check if the character is the fifth character in the pattern
                                    if pattern[0] == pattern[4]:
                                        # if the character is the fifth character in the pattern,
                                        # it means that the position is the fifth position in the list
                                        pattern_list.append(currentPos)
                                    else:
                                        # check if the character is the sixth character in the pattern
                                        if pattern[0] == pattern[5]:
                                            # if the character is the sixth character in the pattern,
                                            # it means that the position is the sixth position in the list
                                            pattern_list.append(currentPos)
                                        else:
                                            # check if the character is the seventh character in the pattern
                                            if pattern[0] == pattern[6]:
                                                # if the character is the seventh character in the pattern,
                                                # it means that the position is the seventh position in the list
                                                pattern_list.append(currentPos)
                                            else:
                                                # check if the character is the eighth character in the pattern
                                                if pattern[0] == pattern[7]:
                                                    # if the character is the eighth character in the pattern,
                                                    # it means that the position is the eighth position in the list
                                                    pattern_list.append(currentPos)
                                                else:
                                                    # check if the character is the ninth character in the pattern
                                                    if pattern[0] == pattern[8]:
                                                       # if the character is the ninth character in the pattern,
                                                       # it means that the position is the ninth position in the list
                                                       pattern_list.append(currentPos)
                                                    else:
                                                       # check if the character is the tenth character in the pattern
                                                       if pattern[0] == pattern[9]:
                                                       # if the character is the tenth character in the pattern,
                                                       # it means that the position is the tenth position in the list
                                                       pattern_list.append(currentPos)
                                                       else:
                                                       # check if the character is the eleventh character in the pattern
                                                       if pattern[0] == pattern[10]:
                                                       # if the character is the eleventh character in the pattern,
                                                       # it means that the position is the eleventh position in the list
                                                       pattern_list.append(currentPos)
                                                       else:
                                                       # check if the character is the twelfth character in the pattern
                                                       if pattern[0] == pattern[11]:
                                                       # if the character is the twelfth character in the pattern,
                                                       # it means that the position is the twelfth position in the list
                                                       pattern_list.append(currentPos)