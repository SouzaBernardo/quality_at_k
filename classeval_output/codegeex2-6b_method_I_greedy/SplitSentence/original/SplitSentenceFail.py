import re
class SplitSentence:  
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """



    def split_sentences(self, sentences_string):
        
        sentences = re.split(r'[.?!]\s', sentences_string)
        return sentences


    def count_words(self, sentences_list):


    def count_words(self, sentence):


    def process_text_file(self, sentences_string):
