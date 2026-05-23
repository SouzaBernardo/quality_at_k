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
        """
        return self.pattern.rfind(char)
    

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        for i in range(self.patLen):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1
    

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []
        last_occurrence = {}
        
        # Preprocessing step: calculate the last occurrence of each character in the pattern
        for i in range(self.patLen):
            last_occurrence[self.pattern[i]] = i
        
        # Searching step: start from the end of the pattern and slide the pattern over the text
        i = self.patLen - 1
        while i < self.textLen:
            j = self.patLen - 1
            
            # Compare characters from right to left
            while j >= 0 and self.pattern[j] == self.text[i - self.patLen + 1 + j]:
                j -= 1
            
            # If the pattern is found, add the position to the list
            if j == -1:
                positions.append(i - self.patLen + 1)
                
                # Shift the pattern to the right by the pattern length
                i += self.patLen
            else:
                # Calculate the shift based on the bad character heuristic
                if self.text[i - self.patLen + 1 + j] in last_occurrence:
                    shift = j - last_occurrence[self.text[i - self.patLen + 1 + j]]
                else:
                    shift = j + 1
                
                # Shift the pattern to the right by the calculated shift
                i += shift
        
        return positions