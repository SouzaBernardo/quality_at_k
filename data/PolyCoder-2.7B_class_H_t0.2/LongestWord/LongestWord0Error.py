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

        if not self.word_list:
            return ''

        # find longest word in the sentence
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word
                break
        return longest_word

    def find_longest_word_in_sentence(self, sentence):
        """
        Find the longest word in a given sentence.
        :param sentence: a sentence str
        :return: longest word in the sentence
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence('I am a student.')
        'a'
        """

        if not self.word_list:
            return ''

        # find longest word in the sentence
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word
                break
        return longest_word

    def find_longest_word_in_sentence_in_word_list(self, sentence):
        """
        Find the longest word in a given sentence in a given word list.
        :param sentence: a sentence str
        :param word_list: a word list
        :return: longest word in the sentence in the word list
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence_in_word_list('I am a student.')
        'a'
        """

        if not self.word_list:
            return ''

        # find longest word in the sentence in the word list
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word
                break
        return longest_word

    def find_longest_word_in_sentence_in_word_list_in_word_list(self, sentence):
        """
        Find the longest word in a given sentence in a given word list in a given word list.
        :param sentence: a sentence str
        :param word_list: a word list
        :param word_list: a word list
        :return: longest word in the sentence in the word list in the word list
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence_in_word_list_in_word_list('I am a student.')
        'a'
        """

        if not self.word_list:
            return ''

        # find longest word in the sentence in the word list in the word list
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word
                break
        return longest_word

    def find_longest_word_in_sentence_in_word_list_in_word_list_in_word_list(self, sentence):
        """
        Find the longest word in a given sentence in a given word list in a given word list in a given word list.
        :param sentence: a sentence str
        :param word_list: a word list
        :param word_list: a word list
        :return: longest word in the sentence in the word list in the word list in the word list
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence_in_word_list_in_word_list_in_word_list('I am a student.')
        'a'
        """

        if not self.word_list:
            return ''

        # find longest word in the sentence in the word list in the word list in the word list
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word