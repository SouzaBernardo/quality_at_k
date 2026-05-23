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
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        """
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = self.get_pos_tag(sentence)
        lemmatized_words = []
        for word, tag in tagged_words:
            if tag.startswith('NN'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='n'))
            elif tag.startswith('VB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='v'))
            elif tag.startswith('JJ'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='a'))
            elif tag.startswith('RB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='r'))
            else:
                lemmatized_words.append(word)
        return lemmatized_words

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        return [tag for word, tag in pos_tags]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))