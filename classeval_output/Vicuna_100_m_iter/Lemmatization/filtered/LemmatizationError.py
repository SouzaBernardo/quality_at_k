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



    def lemmatize_sentence(self, sentence):
        # Remove punctuations of the sentence
        sentence = sentence.replace("'","").replace('"','').replace('`','').replace('[','').replace(']','').replace('{','').replace('}','')
        # tokenizes the input sentence
        words = word_tokenize(sentence)
        # mark the part of speech tag of each word
        tags = pos_tag(words)
        # lemmatizes the words with different parameters based on their parts of speech
        lemmatized_words = []
        for tag in tags:
            if tag.startswith('N'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='n'))
            elif tag.startswith('V'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='v'))
            elif tag.startswith('J'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='a'))
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(tag, pos='n'))
        return lemmatized_words

    def get_pos_tag(self, sentence):
        # Remove punctuations of the sentence
        sentence = sentence.replace("'","").replace('"','').replace('`','').replace('[','').replace(']','').replace('{','').replace('}','')
        # tokenizes the input sentence
        words = word_tokenize(sentence)
        # mark the part of speech tag of each word
        tags = pos_tag(words)
        # lemmatizes the words with different parameters based on their parts of speech
        lemmatized_words = []
        for tag in tags:
            if tag.startswith('N'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='n'))
            elif tag.startswith('V'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='v'))
            elif tag.startswith('J'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='a'))
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(tag, pos='n'))
        return lemmatized_words

    def remove_punctuation(self, sentence):
        # Remove punctuations of the sentence
        sentence = sentence.replace("'","").replace('"','').replace('`','').replace('[','').replace(']','').replace('{','').replace('}','')
        # tokenizes the input sentence
        words = word_tokenize(sentence)
        # mark the part of speech tag of each word
        tags = pos_tag(words)
        # lemmatizes the words with different parameters based on their parts of speech
        lemmatized_words = []
        for tag in tags:
            if tag.startswith('N'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='n'))
            elif tag.startswith('V'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='v'))
            elif tag.startswith('J'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[1:], pos='a'))
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(tag, pos='n'))
        return ' '.join(lemmatized_words)