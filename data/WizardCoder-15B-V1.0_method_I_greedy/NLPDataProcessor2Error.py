from collections import Counter
import re
class NLPDataProcessor2:  
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """







    def process(self, string_list):
        # Define a regular expression pattern to keep only English letters and spaces
        pattern = re.compile('[^a-zA-Z\s]+')
        # Process each string in the list
        word_freq = Counter()
        for string in string_list:
            # Keep only English letters and spaces in the string, and convert to lower case
            string = pattern.sub('', string).lower()
            # Split the string into a list of words and update the word frequency dictionary
            words = string.split()
            word_freq.update(words)
        # Sort the word frequency dictionary by value in descending order and return the top 5 most frequent words
        top_words = dict(word_freq.most_common(5))
        return top_words