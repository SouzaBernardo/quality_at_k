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
        return re.findall(r'[^.?]+[.?]', sentences_string)

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
        words = re.findall(r'\w+', sentence)
        return len(words)

    def process_text_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            sentences = self.split_sentences(text)
            word_counts = [self.count_words(sentence) for sentence in sentences]
            max_word_count = max(word_counts)
        return max_word_count
