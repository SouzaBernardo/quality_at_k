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
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
        # if sentence is empty, return ''
        if len(sentence) == 0:
            return ''

        # if sentence is not empty, split it into words
        if len(sentence) > 0:
            # if sentence is not empty, split it into words
            if len(sentence) > 1:
                # if sentence is not empty, split it into words
                # if sentence is not empty, split it into words
                if sentence[0] =='':
                    # if sentence is not empty, split it into words
                    if sentence[1] =='':
                        # if sentence is not empty, split it into words
                        return self.find_longest_word(sentence[1:])
                    else:
                        # if sentence is not empty, split it into words
                        return self.find_longest_word(sentence[1:])
                else:
                    # if sentence is not empty, split it into words
                    return self.find_longest_word(sentence[1:])
            else:
                # if sentence is not empty, split it into words
                return self.find_longest_word(sentence[1:])
        else:
            # if sentence is empty, return ''
            return ''