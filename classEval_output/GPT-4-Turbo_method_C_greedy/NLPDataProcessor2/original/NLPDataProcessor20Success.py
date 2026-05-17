from collections import Counter
import re
class NLPDataProcessor2: 

    def process_data(self, string_list):
        words_list = []
        for string in string_list:
            string = re.sub('[^a-zA-Z ]', '', string)
            string = string.lower()
            words = string.split()
            words_list.append(words)
        return words_list
    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        # Flatten the list of words lists into a single list
        words = [word for sublist in words_list for word in sublist]
    
        # Calculate the frequency of each word
        word_freq = Counter(words)
    
        # Sort the word frequency dictionary by value in descending order and return the top 5
        word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:5])
    
        return word_freq
    def process(self, string_list):
        words_list = self.process_data(string_list)
        word_frequency = self.calculate_word_frequency(words_list)
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
        top_5_word_frequency = dict(list(sorted_word_frequency.items())[:5])
        return top_5_word_frequency
