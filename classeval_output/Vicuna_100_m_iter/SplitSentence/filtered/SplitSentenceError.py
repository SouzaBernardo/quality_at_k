import re
class SplitSentence:  
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """



    def split_sentences(self, sentences_string):
        sentences_list = sentences_string.split(". ")
        for sentence in sentences_list:
            if "Mr." in sentence:
                continue
            if "?" in sentence:
                sentences_list.remove(sentence)
        return sentences_list

    def count_words(self, sentence):
        words = sentence.split()
        words = [word for word in words if word.isalpha() and word.isalpha() not in ["'", '"', "#", "$", "%", "&", "*", "=", "!", "?", "(", ")", "+" , "-", "."]]
        return len(words)

    def process_text_file(sentences_string):
        sentences_list = split_sentences(sentences_string)
        max_word_count = 0
        for sentence in sentences_list:
            word_count = self.count_words(sentence)
            max_word_count = max(max_word_count, word_count)
        return max_word_count