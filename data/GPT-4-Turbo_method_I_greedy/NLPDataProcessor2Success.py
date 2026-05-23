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
        # Flatten the list of lists into a single list
        flat_list = [word for sublist in words_list for word in sublist]
    
        # Use Counter to calculate word frequency
        word_freq = Counter(flat_list)
    
        # Sort the dictionary by value in descending order and take the top 5
        sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:5])
    
        return sorted_word_freq
    def process(self, string_list):
        # Process the data to get a list of words
        words_list = self.process_data(string_list)
    
        # Calculate the word frequency and return the top 5 most frequent words
        top_5_word_freq = self.calculate_word_frequency(words_list)
    
        return top_5_word_freq