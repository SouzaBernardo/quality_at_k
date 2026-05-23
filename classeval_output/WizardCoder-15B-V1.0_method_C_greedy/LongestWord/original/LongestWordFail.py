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
        # Remove punctuation and convert to lowercase
        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        # Remove any non-alphabetic characters
        word = re.sub(r'[^a-zA-Z]', '', word)
        # Append the word to the word list
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        """
        # Remove punctuation marks
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        # Split sentence into a list of words
        words = sentence.split()
        # Find the longest word in the list that is in the word list
        longest_word = ''
        for word in words:
            if word.lower() in self.word_list and len(word) > len(longest_word):
                longest_word = word
        return longest_word