import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string
class Lemmatization: 
    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()



    def lemmatize_sentence(self, sentence):
        
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        pos_tags = self.get_pos_tag(sentence)
        lemmatized_words = []
        for i in range(len(words)):
            if pos_tags[i][1] == 'NN':
                lemmatized_words.append(self.lemmatizer.lemmatize(words[i], pos='n'))
            elif pos_tags[i][1] == 'VB':
                lemmatized_words.append(self.lemmatizer.lemmatize(words[i], pos='v'))
            elif pos_tags[i][1] == 'JJ':
                lemmatized_words.append(self.lemmatizer.lemmatize(words[i], pos='a'))
            elif pos_tags[i][1] == 'RB':
                lemmatized_words.append(self.lemmatizer.lemmatize(words[i], pos='r'))
            else:
                lemmatized_words.append(self.lemmatizer.lemmatize(words[i]))
        return lemmatized_words


    def get_pos_tag(self, sentence):
        
        sentence = self.remove_punctuation(sentence)
        return pos_tag(word_tokenize(sentence))


    def remove_punctuation(self, sentence):
        
        return sentence.translate(str.maketrans('', '', string.punctuation))