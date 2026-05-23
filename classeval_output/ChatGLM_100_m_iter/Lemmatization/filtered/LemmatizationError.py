import nltk
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string
class Lemmatization:  
    """
    This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.
    """

    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()





    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        punctuations = set()
        punctuations.add('!')
        punctuations.add('?')
        punctuations.add('&')
        punctuations.add('*')
        punctuations.add('(')
        punctuations.add(')')
        punctuations.add('_')
        punctuations.add('{')
        punctuations.add('}')
        tokens = word_tokenize(sentence)
        pos_tags = []
        for token in tokens:
            if token in punctuations:
                continue
            if token.isdigit():
                pos_tags.append('NN')
            elif token.isalpha():
                if token not in self.lemmatizer.lemmatize_word(token):
                    continue
                pos_tags.append('NN')
                if token.lower() in self.lemmatizer.lemmatize_word(token.lower()):
                    pos_tags.append('VBP')
                elif token.lower() in self.lemmatizer.lemmatize_word(token.lower()):
                    pos_tags.append('VBG')
                elif token.lower() in self.lemmatizer.lemmatize_word(token.lower()):
                    pos_tags.append('IN')
                else:
                    pos_tags.append('DT')
            else:
                pos_tags.append(token.lower())
        return pos_tags

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        sentence = sentence.lower() # convert the sentence to lowercase
        pos_tags = self.get_pos_tag(sentence) # get the part of speech tags of each word
        sentence = [word.lower() for word in pos_tags] # remove punctuation from the part of speech tags
        return sentence