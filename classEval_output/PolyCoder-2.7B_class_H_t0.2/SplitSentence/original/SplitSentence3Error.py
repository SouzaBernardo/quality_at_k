import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """


    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """


    def split_text_file(self, text_file_path):
        """
        Split a text file into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param text_file_path: string, path to the text file
        :return:list, split sentence list
        >>> ss.split_text_file("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """


    def process_text_file_with_regex(self, text_file_path, regex_string):
        """
        Given a text, return the number of words in the longest sentence
        :param text_file_path: string, path to the text file
        :param regex_string: string, regex string to be used to split the text file
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file_with_regex("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """


    def split_text_file_with_regex(self, text_file_path, regex_string):
        """
        Split a text file into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param text_file_path: string, path to the text file
        :param regex_string: string, regex string to be used to split the text file
        :return:list, split sentence list
        >>> ss.split_text_file_with_regex("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """


    def process_text_file_with_regex_and_count_words(self, text_file_path, regex_string, count_words_function):
        """
        Given a text, return the number of words in the longest sentence
        :param text_file_path: string, path to the text file
        :param regex_string: string, regex string to be used to split the text file
        :param count_words_function: function, function to be used to count the number of words in the sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file_with_regex_and_count_words("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """


    def split_text_file_with_regex_and_count_words(self, text_file_path, regex_string, count_words_function):
        """
        Split a text file into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param text_file_path: string, path to the text file
        :param regex_string: string, regex string to be used to split the text file
        :param count_words_function: function, function to be used to count the number of words in the sentence
        :return:list, split sentence list
        >>> ss.split_text_file_with_regex_and_count_words("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """


    def process_text_file_with_regex_and_count_words_with_regex(self, text_file_path, regex_string, count_words_function):
        """
        Given a text, return the number of words in the longest sentence
        :param text_file_path: string, path to the text file
        :param regex_string: string, regex string to be used to split the text file
        :param count_words_function: function, function to be used to count the number of words in the sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file_with_regex_and_count_words_with_regex("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """


    def split_text_file_with_regex_and_count_words_with_regex(self, text_file_path, regex_string, count_words_function):
        """
        Split a text file into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param text_file_