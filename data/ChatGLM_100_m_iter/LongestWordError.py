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
        if word not in self.word_list:
            self.word_list.append(word)
        else:
            # Use a regular expression to match the longest word in the sentence
            longest_word = self.word_list.pop(0)
            for word in self.word_list:
                if word.strip() == longest_word.strip():
                    longest_word = word
                    break
            if longest_word not in self.word_list:
                self.word_list.append(longest_word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> sentence = 'I am a student.'
        >>> word_list = longestWord.word_list
        >>> longest_word = sentence.split()
        >>> longest_word_list = []
        >>> for word in word_list:
            if word.strip() == word_list[-1].strip():
                longest_word_list.append(word)
        >>> longest_word = max(word_list, key=word.strip().lower())
        >>> print(longest_word)
        'a'
        """
        # Use a regular expression to match the longest word in the sentence
        regex = re.compile(r'\b\w+\b')
        word_list = sentence.split()
        longest = 0
        for word in word_list:
            if regex.search(word):
                longest = max(longest, word.strip().lower())
        return longest