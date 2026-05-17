import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

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

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """

    def remove_punctuation_from_sentence(self, sentence):
        """
        Removes punctuation from the input sentence.
        :param sentence: a sentence str
        :return: sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_sentence("I am running in a race.")
        'I am running in a race'

        """

    def remove_punctuation_from_word(self, word):
        """
        Removes punctuation from the input word.
        :param word: a word str
        :return: word without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_word("I am running in a race.")
        'I am running in a race'

        """

    def remove_punctuation_from_word_list(self, word_list):
        """
        Removes punctuation from the input word list.
        :param word_list: a word list
        :return: word_list without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_word_list("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """

    def remove_punctuation_from_word_list_with_punctuation(self, word_list):
        """
        Removes punctuation from the input word list.
        :param word_list: a word list
        :return: word_list without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_word_list_with_punctuation("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """

    def remove_punctuation_from_word_list_with_punctuation_list(self, word_list):
        """
        Removes punctuation from the input word list.
        :param word_list: a word list
        :return: word_list without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_word_list_with_punctuation_list("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """

    def remove_punctuation_from_word_list_with_punctuation_list_with_punctuation(self, word_list):
        """
        Removes punctuation from the input word list.
        :param word_list: a word list
        :return: word_list without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_word_list_with_punctuation_list_with_punctuation("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """

    def remove_punctuation_from_word_list_with_punctuation_list_with_punctuation_list(self, word_list):
        """
        Removes punctuation from the input word list.
        :param word_list: a word list
        :return: word_list without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation_from_word_list_with_punctuation_list_with_punctuation("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """

    def remove_punctuation_from_word_list_with_punctuation_list_with_punctuation_list_with_punctuation(self, word_list):
        """
        Removes punctuation from the input word list.
        :param word_list: a word list
        :return: word_list without any punctuation
        >>> lemmatization = Lemmatization()