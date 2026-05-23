import re
import string
class LongestWord: 
    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []



    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """
        if word.lower() in self.word_list:
            return
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        # Remove punctuation marks
        sentence = re.sub(r'[^\w\s]', '', sentence)
        # Split the sentence into a list of words
        words = sentence.split()
        # Iterate through the words
        for word in words:
            # Check if the word is in the word list
            if word in self.word_list:
                # If the word is in the word list, return it
                return word
        # If the word list is empty, return an empty string
        return ''