class BoyerMooreSearch:
    """
    This is a class that implements the Boyer-Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.
    """

    def __init__(self, text, pattern):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

    def match_in_pattern(self, char):
        for i in range(self.patLen-1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        for i in range(self.patLen-1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1

    def bad_character_heuristic(self):
        positions = []
        for i in range(self.textLen - self.patLen + 1):
            mismatchPos = self.mismatch_in_text(i)
            if mismatchPos == -1:
                positions.append(i)
            else:
                matchedPos = self.match_in_pattern(self.text[mismatchPos])
                i = mismatchPos - matchedPos
        return positions