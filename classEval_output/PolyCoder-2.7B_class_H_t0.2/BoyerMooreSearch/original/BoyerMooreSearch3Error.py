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

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2

        """

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

        """

    def find_all_matches(self, text):
        """
        Finds all occurrences of the pattern in the text.
        :param text: The text to be searched, str.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.find_all_matches("ABAABA")
        [0, 3]

        """

    def find_all_matches_in_text(self, text):
        """
        Finds all occurrences of the pattern in the text.
        :param text: The text to be searched, str.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.find_all_matches_in_text("ABAABA")
        [0, 3]

        """

    def find_all_matches_in_text_and_pattern(self, text, pattern):
        """
        Finds all occurrences of the pattern in the text.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.find_all_matches_in_text_and_pattern("ABAABA", "AB")
        [0, 3]

        """

    def find_all_matches_in_text_and_pattern_in_text(self, text, pattern):
        """
        Finds all occurrences of the pattern in the text.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.find_all_matches_in_text_and_pattern_in_text("ABAABA", "AB")
        [0, 3]

        """

    def find_all_matches_in_text_and_pattern_in_text_and_pattern(self, text, pattern, pattern2):
        """
        Finds all occurrences of the pattern in the text.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        :param pattern2: The pattern to be searched for, str.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.find_all_matches_in_text_and_pattern_in_text_and_pattern("ABAABA", "AB")
        [0, 3]

        """

    def find_all_matches_in_text_and_pattern_in_text_and_pattern_in_text(self, text, pattern, pattern2, text2):
        """
        Finds all occurrences of the pattern in the text.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        :param pattern2: The pattern to be searched for, str.
        :param text2: The text to be searched, str.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.find_all_matches_in_text_and_pattern_in_text_and_pattern_in_text("ABAABA", "AB", "AB")
        [0, 3]

        """

    def find_all_matches_in_text_and_pattern_in_text_and_pattern_in_text_and_pattern(self, text, pattern, pattern2, text2, pattern3):
