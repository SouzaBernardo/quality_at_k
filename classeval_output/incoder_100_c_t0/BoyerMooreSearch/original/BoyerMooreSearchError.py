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
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0

        """
        patternLen = self.patLen
        patternPos = self.patPos - 1
        while patternPos >= 0 and patternPos <= patternLen and char == pattern[patternPos]:
            patternPos -= 1
        return patternPos


    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        -1

        """
        patternLen = self.patLen
        patternPos = self.patPos
        while patternPos >= 0 and patternPos <= patternLen and patternPos != currentPos:
            patternPos += 1
        return patternPos


    def search(self):
        """
        Searches the text for the pattern.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.search()
        [0, 3]

        """
        patternLen = self.patLen
        patternPos = self.patPos
        matches = []
        while patternPos >= 0 and patternPos <= patternLen:
            currentPos = self.match_in_pattern(patternPos)
            if currentPos == patternPos:
                matches.append(currentPos)
            patternPos = self.mismatch_in_text(currentPos)
        return matches


class BoyerMooreSearchWithBadCharacters:
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
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0

        """
        patternLen = self.patLen
        patternPos = self.patPos - 1
        while patternPos >= 0 and patternPos <= patternLen and char == pattern[patternPos]:
            patternPos -= 1
        return patternPos

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2

        """
        patternLen = self.patLen
        patternPos = self.patPos
        while patternPos >= 0 and patternPos <= patternLen and patternPos != currentPos:
            patternPos += 1
        return patternPos


    def search(self):
        """
        Searches the text for the pattern.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.search()
        [0, 3]

        """
        patternLen = self.patLen
        patternPos = self.patPos
        matches = []
        while patternPos >= 0 and patternPos <= patternLen:
            currentPos = self.match_in_pattern(patternPos)
            if currentPos == patternPos:
                matches.append(currentPos)
            patternPos = self.mismatch_in_text(currentPos)
        return matches

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

        """
        patternLen = self.patLen
        patternPos = self.patPos
        matches = []
        while patternPos >= 0 and patternPos <= patternLen:
            currentPos = self.match_in_pattern(patternPos)
            if currentPos == patternPos:
                matches.append(currentPos)
            patternPos = self.mismatch_in_text(currentPos)
        return matches


if __name__ == "__main__":
    import doctest
    doctest.testmod()

<|/ file |>
