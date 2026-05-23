class BoyerMooreSearch:  
    """
    his is a class that implements the Boyer-Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.
    """

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
        i = self.patLen - 1
        while i >= 0 and self.pattern[i]!= char:
            i = i - 1
        return i

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        """
        i = self.patLen - 1
        while i >= 0 and self.pattern[i] == self.text[currentPos + i]:
            i -= 1
        if i < 0:
            return -1
        else:
            return currentPos + i

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        result = []
        currentPos = 0
        while currentPos >= 0:
            currentChar = self.text[currentPos]
            i = self.patLen - 1
            while i >= 0 and self.pattern[i] == currentChar:
                i -= 1
                currentPos += 1
            if i < 0:
                result.append(currentPos - self.patLen + 1)
            else:
                currentPos = self.mismatch_in_text(currentPos)
        return result