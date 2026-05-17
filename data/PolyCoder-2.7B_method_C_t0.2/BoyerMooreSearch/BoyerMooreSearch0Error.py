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
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0

        """
        pattern = self.pattern
        text = self.text
        pos = 0
        while pos < self.patLen:
            if text[pos] == pattern[pos]:
                return pos
            pos += 1
        return -1



    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2

        """
        if currentPos == 0:
            return 0
        if currentPos == 1:
            return 1
        if currentPos == self.textLen:
            return self.textLen
        if currentPos == self.patLen:
            return self.patLen
        return -1



    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

        """
        pattern = self.pattern
        text = self.text
        textLen = self.textLen
        patternLen = len(pattern)
        
        # Find all occurrences of the pattern in the text
        for i in range(textLen):
            for j in range(patternLen):
                if pattern[j] == text[i]:
                    break
            else:
                return [i, j]
        return [i, textLen]