from collections import Counter
import re
class NLPDataProcessor2: 


    def process_data(self, string_list):
        """
        Process the list of strings by extracting words, calculating word frequencies, and returning the top 5 most frequent words.
        :param string_list: a list of strings
        :return: a list of top 5 most frequent words
        """
        words_list = []
        for string in string_list:
            # keep only English letters and spaces in the string, then convert the string to lower case
            string = re.sub('[^a-zA-Z\s]', '', string)
            string = string.lower()
            # split the string into a list of words
            words = string.split()
            words_list.append(words)
        # calculate word frequencies
        word_freq = self.calculate_word_frequency(words_list)
        # return the top 5 most frequent words
        top_words = [word for word, freq in word_freq.most_common(5)]
        return top_words

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        word_frequency = Counter()
        for words in words_list:
            word_frequency.update(words)
        return dict(word_frequency.most_common(5))

    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        # concatenate all strings in the list into one string
        all_strings =''.join(string_list)
        # remove non-alphanumeric characters and convert to lower case
        all_strings = re.sub(r'[^a-zA-Z\s]', '', all_strings).lower()
        # split the string into a list of words
        words_list = all_strings.split()
        # calculate the word frequency of each word in the list of words list
        word_frequency = Counter(words_list)
        # sort the word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
        # return the top 5 word frequency dictionary
        return dict(list(sorted_word_frequency.items())[:5])