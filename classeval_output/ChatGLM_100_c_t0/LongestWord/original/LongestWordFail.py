The class LongestWord is designed to allow users to add words to a list and find the longest word in a given sentence. It takes a sentence as input and removes punctuation marks to split it into a list of words. The class is case-sensitive and returns the longest word in the word list. Here's an example of how to use the class:
```python
import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []

    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """

        # Split the sentence into words
        words = re.split(r'\s+', sentence)

        # Initialize the word list
        self.word_list.extend(words)

        # Find the longest word in the word list
        longest_word = max(self.word_list, key=lambda x: len(x))

        # Return the longest word
        return longest_word
```
In this example, the `find_longest_word` method splits the sentence into words using the `\s+` regular expression, and then uses the `max` function to find the longest word in the word list. If the word list is empty, it returns an empty string.