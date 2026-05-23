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

        if len(sentence) == 0:
            return ''

        if len(sentence) == 1:
            return sentence

        # find longest word in sentence
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word
                break

        # if there is no word in sentence, return ''
        if not longest_word:
            return ''

        # if there is a word in sentence, return it
        if len(longest_word) > 0:
            return longest_word

        # if there is no word in sentence, return ''
        return ''

    def find_longest_word_in_sentence(self, sentence):
        """
        Find the longest word in a sentence.
        :param sentence: a sentence str
        :return str: longest word in the sentence. return '' if sentence is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence('I am a student.')
        'a'
        """

        if len(sentence) == 0:
            return ''

        if len(sentence) == 1:
            return sentence

        # find longest word in sentence
        longest_word = ''
        for word in sentence:
            if word in self.word_list:
                longest_word = word
                break

        # if there is no word in sentence, return ''
        if not longest_word:
            return ''

        # if there is a word in sentence, return it
        if len(longest_word) > 0:
            return longest_word

        # if there is no word in sentence, return ''
        return ''

    def find_longest_word_in_sentence_in_list(self, sentence, list):
        """
        Find the longest word in a sentence in a list.
        :param sentence: a sentence str
        :param list: a list of words
        :return str: longest word in the sentence in the list. return '' if sentence is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence_in_list('I am a student.', ['a','m'])
        'a'
        """

        if len(sentence) == 0:
            return ''

        if len(sentence) == 1:
            return sentence

        # find longest word in sentence in a list
        longest_word = ''
        for word in sentence:
            if word in list:
                longest_word = word
                break

        # if there is no word in sentence, return ''
        if not longest_word:
            return ''

        # if there is a word in sentence, return it
        if len(longest_word) > 0:
            return longest_word

        # if there is no word in sentence, return ''
        return ''

    def find_longest_word_in_sentence_in_list_in_list(self, sentence, list, list_length):
        """
        Find the longest word in a sentence in a list.
        :param sentence: a sentence str
        :param list: a list of words
        :param list_length: the length of the list
        :return str: longest word in the sentence in the list. return '' if sentence is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word_in_sentence_in_list_in_list('I am a student.', ['a','m'])
        'a'
        """

        if len(sentence) == 0:
            return ''

        if len(sentence) == 1:
            return sentence

        # find longest word in sentence in a list
        longest_word = ''
    