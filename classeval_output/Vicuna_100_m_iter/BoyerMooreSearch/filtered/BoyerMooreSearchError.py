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
        pattern = self.pattern
        patternLen = self.patLen
        for i in range(self.textLen):
            if pattern[i] == char:
                return i
            elif pattern[i] == self.pattern[i]:
                continue
            else:
                break
        return patternLen

    def mismatch_in_text(self, currentPos):
        pattern = self.pattern
        patternLen = self.patLen
        for i in range(self.textLen):
            if pattern[i] != self.text[i]:
                return i
        return -1

    def bad_character_heuristic(self):
        pattern = self.pattern
        patternLen = self.patLen
        positions = []
        for i in range(self.textLen):
            if pattern[i] == pattern[i + 1]:
                continue
            if pattern[i] == self.pattern[i]:
                positions.append(i)
            else:
                positions.append(self.match_in_pattern(pattern[i]))
        return positions