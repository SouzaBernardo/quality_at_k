from collections import Counter
import re
class NLPDataProcessor2: 


    def process_data(self, string_list):
        # keep only English letters and spaces in the string
        string_list = [word.lower() for word in string_list if word.isalpha()]
        # split the string into a list of words
        words_list = string_list[0].split()
        # calculate the frequency of each word
        word_freq = Counter(words_list)
        # return the top 5 most frequent words
        top_words = word_freq.most_common(5)
        return top_words

    def calculate_word_frequency(self, words_list):
        word_frequency = Counter()
        for word in words_list:
            for sub_word in word:
                word_frequency[sub_word] += 1
        sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_frequency

    def process(self, string_list):
        # keep only English letters and spaces in the string
        string_list = [word.lower() for word in string_list if word.isalpha()]
        # convert the string to lower case
        string_list = [word.lower() for word in string_list]
        # split the string into a list of words
        string_list = [word.split(" ") for word in string_list]
        # calculate the word frequency of each word in the list of words list
        word_freq = Counter(string_list)
        # sort the word frequency dictionary by value in descending order
        word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        # return the top 5 word frequency dictionary
        return word_freq[:5]