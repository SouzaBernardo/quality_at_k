
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
        for i in range(self.patLen - 1, -1, -1):
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
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1
    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        # Create the bad character list
        bad_char = [-1]*256
        for i in range(self.patLen):
            bad_char[ord(self.pattern[i])] = i
    
        # Initialize variables
        s = 0
        positions = []
    
        while(s <= self.textLen - self.patLen):
            j = self.patLen - 1
    
            # Keep reducing index j of pattern while characters of pattern and text are matching at this shift s
            while j >= 0 and self.pattern[j] == self.text[s + j]:
                j -= 1
    
            # If the pattern is present at current shift, then index j will become -1 after the above loop
            if j < 0:
                positions.append(s)
                s += (self.patLen - bad_char[ord(self.text[s + self.patLen])] if s + self.patLen < self.textLen else 1)
            else:
                # Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern.
                s += max(1, j - bad_char[ord(self.text[s + j])])
    
        return positions
