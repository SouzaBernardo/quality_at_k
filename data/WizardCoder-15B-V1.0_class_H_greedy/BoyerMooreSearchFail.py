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







boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
print(boyerMooreSearch.bad_character_heuristic()) # Output: [0, 3]