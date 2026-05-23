
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
        return self.pattern.rfind(char)
    

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1
    

    def bad_character_heuristic(self):
        positions = []
        i = 0
        while i <= self.textLen - self.patLen:
            j = self.patLen - 1
            while j >= 0 and self.pattern[j] == self.text[i + j]:
                j -= 1
            if j == -1:
                positions.append(i)
                i += 1
            else:
                mismatchPos = self.mismatch_in_text(i + j)
                if mismatchPos == -1:
                    i += self.patLen
                else:
                    shift = j - self.match_in_pattern(self.text[mismatchPos])
                    i += max(1, shift)
        return positions
    