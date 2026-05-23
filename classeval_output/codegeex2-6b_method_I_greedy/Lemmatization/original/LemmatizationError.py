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
        
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(sentence)
        pos_words = pos_tag(words)
        lemmatized_words = []
        for word, pos in pos_words:
            if pos.startswith('NN'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='n'))
            elif pos.startswith('VB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='v'))
            elif pos.startswith('JJ'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='a'))
            elif pos.startswith('RB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='r'))
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(word))
        return lemmatized_words


    def get_pos_tag(self, sentence):
        
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(sentence)
        pos_words = pos_tag(words)
        return [pos for word, pos in pos_words]


    def remove_punctuation(self, sentence):
        
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        return sentence
