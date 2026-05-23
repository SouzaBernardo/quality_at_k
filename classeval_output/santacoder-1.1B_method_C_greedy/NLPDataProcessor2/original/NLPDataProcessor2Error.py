from collections import Counter
import re
class NLPDataProcessor2: 


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
            string = re.sub(r'[^\w\s]', '', string)
            string = string.lower()
            words = string.split()
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
        word_frequency = Counter(words_list)
        word_frequency = dict(word_frequency.most_common(5))
        return word_frequency


    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        # keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        words_list = [re.sub('[^a-zA-Z ]', '', word) for word in string_list]
        # convert the string to lower case
        words_list = [word.lower() for word in words_list]
        # split the string into a list of words
        words_list = [word.split() for word in words_list]
        # calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        word_frequency = self.calculate_word_frequency(words_list)
        # keep only the top 5 most frequent words
        top_5_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
        # create a dictionary of word frequency, key is word, value is frequency
        word_frequency_dict = dict(top_5_words)
        return word_frequency_dict
