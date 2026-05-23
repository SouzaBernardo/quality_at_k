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
        sentences = re.findall(r'\b(\w+)\b', sentences_string)
        word_count = len(sentences)
        return sentences, word_count

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
        # Split the sentence into words using regular expressions
        words = re.findall(r'\b\w+\b', sentence)

        # Calculate the number of non-empty words
        non_empty_words = sum([1 for word in words if word!= " "])

        # Calculate the number of empty words
        empty_words = sum([0 for word in words if word == " "])

        # Return the total number of words
        return non_empty_words + empty_words

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        sentences = re.split(" ", sentences_string)
        max_sentence = max(sentences)
        word_count = len(sentences[max_sentence.index():])
        return word_count