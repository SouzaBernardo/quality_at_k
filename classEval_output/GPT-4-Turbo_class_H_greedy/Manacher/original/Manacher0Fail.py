```python
class Manacher:
    """
    This is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            diff += 1
        return diff

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        string = '|'.join('^{}$'.format(self.input_string))
        length = [0] * len(string)
        center = right = 0

        for i in range(1, len(string) - 1):
            if i < right:
                length[i] = min(right - i, length[2 * center - i])

            length[i] = self.palindromic_length(i, length[i], string)
            if i + length[i] > right:
                center, right = i, i + length[i]

        max_length, center = max((n, i) for i, n in enumerate(length))
        return self.input_string[(center - max_length) // 2: (center + max_length) // 2]
```