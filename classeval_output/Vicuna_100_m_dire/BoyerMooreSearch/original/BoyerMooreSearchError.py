
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
        pattern = self.pattern
        patternLen = self.patLen
        for i in range(self.textLen):
            if pattern[i] != char:
                continue
            j = i + 1
            while j < patternLen and pattern[j] == char:
                j += 1
            return j

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int, otherwise -1.
        """
        patternChars = self.pattern
        textChars = self.text
        patternLen = len(pattern)
        textLen = len(self.text)
        if currentPos >= patternLen or currentPos >= textLen:
            return -1
        if patternChars[currentPos] != textChars[currentPos]:
            return currentPos
        currentPos += 1
        while currentPos < patternLen and patternChars[currentPos] == textChars[currentPos]:
            currentPos += 1
        return currentPos

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        pattern = self.pattern
        text = self.text
        patternLen = len(pattern)
        textLen = len(text)
        positions = []
        for i in range(textLen):
            if pattern[i] == text[i]:
                continue
            else:
                positions.append(i)
        return positions