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
        """
        words_list = []
        for string in string_list:
            # keep only English letters and spaces in the string
            string = re.sub(r'[^a-zA-Z\s]', '', string)
            # convert the string to lower case
            string = string.lower()
            # split the string into a list of words
            words = string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        word_frequency = Counter()
        for words in words_list:
            for word in words:
                word_frequency[word] += 1
        # sort the word frequency dictionary by value in descending order
        top_words = dict(word_frequency.most_common(5))
        return top_words

    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        words_list = self.process_data(string_list)
        top_words = self.calculate_word_frequency(words_list)
        return top_words




nlp_processor = NLPDataProcessor2()
string_list = ['This is a test.', 'This is another test.']
top_words = nlp_processor.process(string_list)
print(top_words)


Output:


{'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}