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
            string = re.sub(r'[^a-zA-Z ]+', '', string)
            string_list = string.lower().split()
            words_list.append(string_list)
        return words_list


    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        word_frequency = {}
        for words in words_list:
            for word in words:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
        sorted_word_frequency = sorted(word_frequency.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_word_frequency[0:5]


    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        
        words_list = [word for string in string_list for word in re.findall(r'\w+', string)]
        
        word_frequency_dict = {}
        for word in words_list:
            if word in word_frequency_dict:
                word_frequency_dict[word] += 1
            else:
                word_frequency_dict[word] = 1
        
        sorted_word_frequency_dict = sorted(word_frequency_dict.items(), key=lambda kv: kv[1], reverse=True)
        
        return sorted_word_frequency_dict[:5]