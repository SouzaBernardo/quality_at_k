
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
        for i in range(self.patLen-1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1
    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        """
        for i in range(self.patLen-1, -1, -1):
            if self.text[currentPos + i] != self.pattern[i]:
                return currentPos + i
        return -1
    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        positions = []  # Output variable
        currentPos = 0  # Start from the beginning of the text
    
        while currentPos <= self.textLen - self.patLen:
            mismatchPos = self.mismatch_in_text(currentPos)
            if mismatchPos == -1:
                positions.append(currentPos)
                currentPos += self.patLen
            else:
                matchPos = self.match_in_pattern(self.text[mismatchPos])
                currentPos = mismatchPos - matchPos if mismatchPos - matchPos > 0 else 1
    
        return positions
    
