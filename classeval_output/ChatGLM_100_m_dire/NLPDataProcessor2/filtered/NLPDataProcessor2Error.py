from collections import Counter
import re
class NLPDataProcessor2: 




    def calculate_word_frequency(self, words_list):
        word_frequency_dict = Counter(words_list)
        word_frequency_dict.sort(reverse=True)
        return word_frequency_dict

    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1, 'test': 1}
        """
        # Keep only English letters and spaces in the string
        string_list = [re.sub('[a-zA-Z]+', '', s) for s in string_list]
        # Convert the string to lower case
        string_list = [s.lower() for s in string_list]
        # Split the string into a list of words
        words = list(string_list.split())
        # Calculate the word frequency of each word in the list of words
        word_frequency_dict = {}
        for word in words:
            word_frequency_dict[word] = word_frequency_dict.get(word, 0) + 1
        # Sort the word frequency dictionary by value in descending order
        word_frequency_dict.sort(key=lambda x: x[-1])
        # Return the top 5 most frequent words
        return word_frequency_dict[:5]