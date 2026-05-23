from collections import Counter
import re
class NLPDataProcessor2: 


    def process_data(self, string_list):
        

        words_list = []
        for string in string_list:
            string = re.sub(r'[^a-zA-Z ]', '', string)
            string = string.lower()
            words_list.append(string.split())
        return words_list


    def calculate_word_frequency(self, words_list):


    def process(self, string_list):
        
        words_list = []
        for string in string_list:
            string = re.sub(r'[^a-zA-Z\s]', '', string)
            string = string.lower()
            words_list.extend(string.split())

        word_frequency = self.calculate_word_frequency(words_list)
        word_frequency_sorted = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        return word_frequency_sorted[:5]