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
        if char == self.pattern[self.patLen - 1]:
            return self.patLen - 1
        else:
            return self.mismatch_in_text(self.textLen - 1)



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
        if currentPos == 2:
            return 2
        if currentPos == 3:
            return 3
        if currentPos == 4:
            return 4
        if currentPos == 5:
            return 5
        if currentPos == 6:
            return 6
        if currentPos == 7:
            return 7
        if currentPos == 8:
            return 8
        if currentPos == 9:
            return 9
        if currentPos == 10:
            return 10
        if currentPos == 11:
            return 11
        if currentPos == 12:
            return 12
        if currentPos == 13:
            return 13
        if currentPos == 14:
            return 14
        if currentPos == 15:
            return 15
        if currentPos == 16:
            return 16
        if currentPos == 17:
            return 17
        if currentPos == 18:
            return 18
        if currentPos == 19:
            return 19
        if currentPos == 20:
            return 20
        if currentPos == 21:
            return 21
        if currentPos == 22:
            return 22
        if currentPos == 23:
            return 23
        if currentPos == 24:
            return 24
        if currentPos == 25:
            return 25
        if currentPos == 26:
            return 26
        if currentPos == 27:
            return 27
        if currentPos == 28:
            return 28
        if currentPos == 29:
            return 29
        if currentPos == 30:
            return 30
        if currentPos == 31:
            return 31
        if currentPos == 32:
            return 32
        if currentPos == 33:
            return 33
        if currentPos == 34:
            return 34
        if currentPos == 35:
            return 35
        if currentPos == 36:
            return 36
        if currentPos == 37:
            return 37
        if currentPos == 38:
            return 38
        if currentPos == 39:
            return 39
        if currentPos == 40:
            return 40
        if currentPos == 41:
            return 41
        if currentPos == 42:
            return 42
        if currentPos == 43:
            return 43
        if currentPos == 44:
            return 44
        if currentPos == 45:
            return 45
        if currentPos == 46:
            return 46
        if currentPos == 47:
            return 47
        if currentPos == 48:
            return 48
        if currentPos == 49:
            return 49
        if currentPos == 50:
            return 50
        if currentPos == 51:
            return 51
        if currentPos == 52:
            return 52
        if currentPos == 53:
            return 53
        if currentPos == 54:
            return 54
        if currentPos == 55:
            return 55
        if currentPos == 56:
            return 56
        if currentPos == 57:
        

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
        textLen = len(text)
        patternLen = len(pattern)
        
        # find all occurrences of pattern in text
        pos = 0
        while pos < textLen:
            if text[pos] == pattern[0]:
                pos += 1
                continue
            
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[i]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue
                
            # find all occurrences of pattern in text
            for i in range(1, patternLen):
                if text[pos+i] == pattern[patternLen-i-1]:
                    pos += i
                    continue