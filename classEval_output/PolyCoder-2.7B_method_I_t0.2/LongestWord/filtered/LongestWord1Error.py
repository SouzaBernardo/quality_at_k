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
        self.word_list.append(word)




    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
        if len(sentence) == 0:
            return ''
        
        # find longest word in sentence
        longest_word = ''
        for word in self.word_list:
            if word in sentence:
                longest_word = word
                break
        
        # if there is no word in sentence, return ''
        if not longest_word:
            return ''
        
        # if there is a word in sentence, remove punctuation marks and split the sentence into a list of words
        if len(sentence) > len(longest_word):
            return longest_word
        
        # if there is a word in sentence, split the sentence into a list of words
        return self.split_sentence(sentence)