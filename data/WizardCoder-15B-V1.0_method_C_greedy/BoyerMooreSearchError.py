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
        rightmost = -1
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                rightmost = i
        return rightmost

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        """
        i = self.patLen - 1
        while i >= 0:
            if self.pattern[i]!= self.text[currentPos + i]:
                return currentPos + i
            i -= 1
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the "bad character" heuristic.
        :return: A list of all positions of the pattern in the text, list.
        """
        skip = [0] * 256
        for i in range(self.patLen):
            skip[ord(self.pattern[i])] = self.patLen - i - 1
    
        currentPos = self.patLen - 1
        result = []
    
        while currentPos < self.textLen:
            if self.text[currentPos] == self.pattern[self.patLen - 1]:
                match = True
                for i in range(self.patLen - 2, -1, -1):
                    if self.text[currentPos - i]!= self.pattern[i]:
                        match = False
                        break
                if match:
                    result.append(currentPos - self.patLen + 1)
                    currentPos += self.patLen
                else:
                    currentPos += skip[ord(self.text[currentPos])]
            else:
                currentPos += skip[ord(self.text[currentPos])]
    
        return result