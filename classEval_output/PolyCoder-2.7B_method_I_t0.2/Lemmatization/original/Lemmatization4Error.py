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
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """
        # lemmatize the sentence
        sentence = self.lemmatize(sentence)
        # remove punctuation
        sentence = self.remove_punctuation(sentence)
        # lemmatize the tokens
        sentence = self.lemmatize_tokens(sentence)
        # store the lemmatized sentence
        return sentence



    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """
        # lemmatize the sentence
        sentence = self.lemmatize(sentence)
        # remove punctuation
        sentence = self.remove_punctuation(sentence)
        # lemmatize the tokens
        sentence = self.lemmatize_tokens(sentence)
        # store the lemmatized sentence
        return sentence




    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
        # remove punctuation
        sentence = sentence.strip()
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
        # remove punctuation
        sentence = sentence.replace(' ', '')
     