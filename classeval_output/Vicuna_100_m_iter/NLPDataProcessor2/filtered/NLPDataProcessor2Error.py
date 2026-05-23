from collections import Counter
import re
class NLPDataProcessor2:  
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """



    def process_data(self, string_list):
        # Keep only English letters and spaces in the string
        string_list = [word.lower() for word in string_list if word.isalpha()]
        # Convert the string to lower case
        string_list = [word.lower() for word in string_list]
        # Split the string into a list of words
        words_list = string_list.split()
        # Calculate the frequency of each word
        word_freq = Counter(words_list)
        # Return the top 5 most frequent words
        top_words = word_freq.most_common(5)
        return top_words

    def calculate_word_frequency(self, words_list):
        # Keep only English letters and spaces in the string
        words_list = [word.lower() for word in words_list if word.isalpha()]
        # Convert the string to lower case
        words_list = [word.lower() for word in words_list]
        # Split the string into a list of words
        words_list = string_list.split()
        # Calculate the frequency of each word
        word_freq = Counter(words_list)
        # Sort the word frequency dictionary by value in descending order
        word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return word_freq

    def process(self, string_list):
        # Keep only English letters and spaces in the string
        string_list = [word.lower() for word in string_list if word.isalpha()]
        # Convert the string to lower case
        string_list = [word.lower() for word in string_list]
        # Split the string into a list of words
        words_list = string_list.split()
        # Calculate the frequency of each word
        word_freq = Counter(words_list)
        # Sort the word frequency dictionary by value in descending order
        word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return word_freq