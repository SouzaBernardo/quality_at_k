import re
class SplitSentence: 


    def split_sentences(self, sentences_string):
        sentences = sentences_string.split()
        sentences = [sentence for sentence in sentences if sentence.endswith('.') or sentence.endswith('?') and sentence.strip().endswith(' ')]
        return sentences

    def count_words(self, sentence):
        words = sentence.split()
        words = [word for word in words if word.isalpha() and word.isalpha()]
        word_count = len(words)
        return word_count

    def process_text_file(self, sentences_string):
        max_word_count = 0
        longest_sentence = ""
        for sentence in sentences_string.split("\n"):
            if len(sentence) > max_word_count:
                max_word_count = len(sentence)
                longest_sentence = sentence
        return max_word_count