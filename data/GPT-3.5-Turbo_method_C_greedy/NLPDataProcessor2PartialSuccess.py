from collections import Counter
import re
class NLPDataProcessor2: 


    def process_data(self, string_list):
        words_list = []
        for string in string_list:
            # Keep only English letters and spaces
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
            # Convert the string to lower case
            lower_case_string = cleaned_string.lower()
            # Split the string into a list of words
            words = lower_case_string.split()
            words_list.append(words)
        return words_list
    

    def calculate_word_frequency(self, words_list):
        # Calculate word frequency using Counter
        word_counts = Counter(word for sublist in words_list for word in sublist)

        # Sort the word frequency dictionary by value in descending order
        sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

        # Get the top 5 most frequent words
        top_5_words = dict(list(sorted_word_counts.items())[:5])

        return top_5_words