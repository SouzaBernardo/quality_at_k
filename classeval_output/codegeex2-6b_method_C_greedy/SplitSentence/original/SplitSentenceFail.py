import re
class SplitSentence: 


    def split_sentences(self, sentences_string):
        
        sentences = re.split(r'[.?!]\s', sentences_string)
        return sentences


    def count_words(self, sentence):


    def process_text_file(self, sentences_string):
