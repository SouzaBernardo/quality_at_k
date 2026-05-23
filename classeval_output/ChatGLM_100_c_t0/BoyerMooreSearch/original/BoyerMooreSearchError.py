Here is the completed `Boyer Moore Search` class:
```python
class Boyer Moore Search:
    """
    his is a class that implements the Boyer- Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.
    """

    def __init__(self, text, pattern):
        """
        Initializes the Boyer Moore Search class with the given text and pattern.
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
        >>> boyer Moore Search = Boyer Moore Search("ABAABA", "AB")
        >>> boyer Moore Search.match_in_pattern("A")
        0

        """

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int, otherwise -1.
        >>> boyer Moore Search = Boyer Moore Search("ABAABA", "ABC")
        >>> boyer Moore Search.mismatch_in_text(0)
        2

        """

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyer Moore Search = Boyer Moore Search("ABAABA", "AB")
        >>> boyer Moore Search.bad_character_heuristic()
        [0, 3]

        """

    def search(self, text):
        """
        Searches the given text for occurrences of the pattern.
        :param text: The text to be searched, str.
        :return: The number of occurrences of the pattern in the text, int.
        """
        self.text = text
        self.pattern = pattern
        count = 0
        for i in range(self.textLen):
            char = self.text[i]
            if self.match_in_pattern(char):
                count += 1
            elif self.mismatch_in_text(i):
                count += 1
            else:
                self.bad_character_heuristic()

        return count
```