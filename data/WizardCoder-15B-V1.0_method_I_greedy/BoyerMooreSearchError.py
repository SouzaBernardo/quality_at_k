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
        rightmost = self.patLen - 1
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == self.text[currentPos + i]:
                rightmost = i
        if rightmost == -1:
            return -1
        else:
            return currentPos + rightmost + 1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        rightmost = [self.match_in_pattern(char) for char in self.pattern]
        result = []
        i = 0
        while i <= self.textLen - self.patLen:
            j = self.patLen - 1
            while j >= 0 and self.pattern[j] == self.text[i + j]:
                j -= 1
            if j < 0:
                result.append(i)
            i += max(1, j - rightmost[j])
        return result