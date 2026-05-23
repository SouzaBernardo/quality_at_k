import re
import string
class LongestWord: 
    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []



    def add_word(self, word):


    def find_longest_word(self, sentence):
        
        sentence = sentence.lower()
        sentence = re.sub(r'[^\w\s]', '', sentence)
        sentence = sentence.split()
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word