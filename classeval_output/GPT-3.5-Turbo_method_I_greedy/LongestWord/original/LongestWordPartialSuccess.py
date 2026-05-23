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
        Append the input word into self.word_list.
        :param word: str, input word
        """
        self.word_list.append(word)
    

    def find_longest_word(self, sentence):
        # Remove punctuation marks from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Split the sentence into a list of words
        words = sentence.split()
        
        # Initialize the longest word as an empty string
        longest_word = ''
        
        # Iterate through each word in the list
        for word in words:
            # Check if the word is in the word list
            if word in self.word_list:
                # Check if the length of the current word is greater than the length of the longest word
                if len(word) > len(longest_word):
                    longest_word = word
        
        # Return the longest word
        return longest_word
    