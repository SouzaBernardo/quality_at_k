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
        """
        return re.split(r'(?<=[^A-Z].[.?])\s+(?=[A-Z])', sentences_string)



    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        """
        sentence_list = self.split_sentences(sentences_string)
        max_sentence_length = 0
        for sentence in sentence_list:
            sentence_length = len(sentence.split())
            if sentence_length > max_sentence_length:
                max_sentence_length = sentence_length
        return max_sentence_length