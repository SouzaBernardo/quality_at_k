import re
class SplitSentence: 


    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        sentences_list = re.split(r'(?<=[.\?])\s', sentences_string)
        return sentences_list

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
        return len(sentence.split())

    def process_text_file(self, sentences_string):
        """
        Process a given text file to find the maximum word count
        :param sentences_string: string, the text to process
        :return: int, the maximum number of words in a sentence
        """
        longest_sentence = ""
        max_words = 0
        sentences = self.split_sentences(sentences_string)
        for sentence in sentences:
            words = self.count_words(sentence)
            if words > max_words:
                max_words = words
                longest_sentence = sentence
        return max_words, longest_sentence