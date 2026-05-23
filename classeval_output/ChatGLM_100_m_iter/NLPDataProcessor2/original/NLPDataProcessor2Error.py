from collections import Counter
import re
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
        # Convert the string to lowercase
        string_list = list(map(lambda x: x.lower(), string_list))

        # Split the string into a list of words
        words_list = list(map(lambda x: re.findall(r'\w+', x), string_list))

        # Calculate the frequency of each word
        word_counts = Counter(words_list)

        # Return the top 5 most frequent words
        return word_counts.most_common(5)

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        top_words = {word: word_counts.value for word, word_counts in zip(words_list, word_counts.items())}
        top_words.sort(key=lambda x: x[1], reverse=True)
        return top_words

    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lowercase, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        # Convert the string to lowercase
        string_list = list(map(lambda x: x.lower(), string_list))

        # Split the string into a list of words
        words_list = list(map(lambda x: re.findall(r'\w+', x), string_list))

        # Calculate the word frequency of each word
        word_counts = Counter(words_list)

        # Return the top 5 most frequent words
        return word_counts.most_common(5)