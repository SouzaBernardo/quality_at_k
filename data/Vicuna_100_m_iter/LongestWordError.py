import re
import string
class LongestWord:  
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

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
            return True
        self.word_list.append(word)
        return True

    def find_longest_word(self, sentence):
        # Remove punctuation marks
        sentence = re.sub('[^\w\s]', '', sentence)
        # Split the sentence into a list of words
        words = sentence.split()
        # Iterate through the words
        for word in words:
            # Check if the word is in the word list
            if word.lower() in self.word_list:
                # If it is, return the word
                return word
        return ''