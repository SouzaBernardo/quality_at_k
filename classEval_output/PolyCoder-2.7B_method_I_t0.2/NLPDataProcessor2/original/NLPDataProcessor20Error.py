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
        words_list = []
        for string in string_list:
            string = string.lower()
            if string in self.nlp_dict:
                words_list.append(self.nlp_dict[string])
            else:
                words_list.append([])
        return words_list


    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        top5_dict = {}
        for word in words_list:
            if word in top5_dict:
                top5_dict[word] += 1
            else:
                top5_dict[word] = 1
        top5_dict = sorted(top5_dict.items(), key=lambda x: x[1], reverse=True)
        return top5_dict



    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        words_list = []
        for string in string_list:
            string = string.lower()
            if string in self.nlp_dict:
                words_list.append(self.nlp_dict[string])
            else:
                words_list.append([])
        return self.calculate_word_frequency(words_list)

