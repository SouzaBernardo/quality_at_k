Here is the completed code for the class NLPDataProcessor2:

```python
import re
from collections import Counter

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        >>> NLPDataProcessor.process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
        words_list = []
        for string in string_list:
            words = re.findall(r'[a-zA-Z ]', string.lower())
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        word_frequency = Counter()
        for words in words_list:
            word_frequency.update(words)
        top_5_words = dict(word_frequency.most_common(5))
        return top_5_words

    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        words_list = self.process_data(string_list)
        top_5_words = self.calculate_word_frequency(words_list)
        return top_5_words
```

This code completes the class NLPDataProcessor2 by implementing the `process_data`, `calculate_word_frequency`, and `process` methods. The `process_data` method takes a list of strings, keeps only English letters and spaces, converts the string to lowercase, and splits the string into a list of words. The `calculate_word_frequency` method calculates the word frequency of each word in the list of words lists and returns the top 5 most frequent words. The `process` method combines the functionality of `process_data` and `calculate_word_frequency` to process a list of strings and return the top 5 word frequency dictionary.