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
        if word not in self.word_list:
            self.word_list.append(word)
        else:
            self.word_list.sort(key=lambda x: x.split()[-1])
            longest = self.word_list[-1]
            for word in self.word_list[:-1]:
                if word.strip()!= word:
                    if len(self.word_list) > len(word):
                        longest = word
                        break
            if longest!= self.find_longest_word(sentence):
                self.find_longest_word(sentence)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.', case=False)
        'A'
        """
        if not self.word_list:
            return ''
        for word in sentence.split():
            if word in self.word_list:
                return word
        return ''