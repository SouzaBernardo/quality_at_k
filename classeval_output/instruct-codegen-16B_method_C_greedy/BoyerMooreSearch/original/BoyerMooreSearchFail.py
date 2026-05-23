
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
        i = self.patLen - 1
        while i >= 0 and self.pattern[i]!= char:
            i = i - 1
        return i

    def mismatch_in_text(self, currentPos):
        mismatch = 0
        for i in range(self.patLen):
            if self.pattern[i]!= self.text[currentPos + i]:
                mismatch = i
                break
        if mismatch == 0:
            return currentPos + self.patLen
        else:
            # Calculate shift offset
            shiftOffset = 1
            while(self.pattern[mismatch - shiftOffset] == self.text[currentPos + self.patLen - shiftOffset]):
                shiftOffset += 1
            return currentPos + self.patLen - shiftOffset

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        result = []
        for i in range(self.textLen - self.patLen + 1):
            mismatches = 0
            for j in range(self.patLen):
                if self.text[i+j]!= self.pattern[j]:
                    mismatches += 1
            if mismatches <= 1:
                result.append(i)
        return result