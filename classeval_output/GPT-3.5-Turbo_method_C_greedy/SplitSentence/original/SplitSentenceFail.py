import re
class SplitSentence: 


    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        # Use regular expression to split sentences
        sentence_list = re.split(r'(?<=[.?!])\s', sentences_string)
        return sentence_list


    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
        words = sentence.split()
        count = 0
        for word in words:
            if re.match("^[a-zA-Z]+$", word):
                count += 1
        return count


    def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        max_word_count = 0
    
        for sentence in sentences:
            word_count = self.count_words(sentence)
            if word_count > max_word_count:
                max_word_count = word_count
    
        return max_word_count
    