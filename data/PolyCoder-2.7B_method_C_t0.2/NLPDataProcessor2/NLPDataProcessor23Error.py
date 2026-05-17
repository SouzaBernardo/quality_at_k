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
        for word in string_list:
            if re.search('[^a-zA-Z0-9]', word):
                words_list.append(word)
            else:
                words_list.append(word.lower())
        return words_list




    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        return sorted(self.get_frequency_dict(words_list), key=lambda x: x[1], reverse=True)


    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)
        self.calculate_word_frequency(string_list)
        self.process_data(string_list)