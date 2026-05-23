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
        self.word_list.append(word)
    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        """
        if not self.word_list:
            return ''
        
        # Remove punctuation from the sentence
        sentence = re.sub('['+string.punctuation+']', '', sentence)
        
        # Split the sentence into words
        words = sentence.split()
        
        # Find the longest word in the word list that is also in the sentence
        longest_word = max((word for word in self.word_list if word in words), key=len, default='')
        
        return longest_word