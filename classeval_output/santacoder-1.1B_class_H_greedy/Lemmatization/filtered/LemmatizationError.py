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

    def remove_stopwords(self, sentence):
        """
        Removes stopwords from the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_stopwords("I am running in a race.")
        'I am running in a race'

        """

    def lemmatize_and_remove_stopwords(self, sentence):
        """
        Removes stopwords from the input text and lemmatizes the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords and lemmatized
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text and lemmatizes the input text.
        :param sentence: a sentence str
        :return: str, sentence without punctuation and lemmatized
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_punctuation("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, and removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, and without punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords_and_punctuation("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation_and_stem(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, removes punctuation from the input text, and stems the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, without punctuation, and stems the input text
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords_and_punctuation_and_stem("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, removes punctuation from the input text, stems the input text, and part-of-speech tag the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, without punctuation, stems the input text, and part-of-speech tag the input text
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, removes punctuation from the input text, stems the input text, part-of-speech tag the input text, and lemmatizes the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, without punctuation, stems the input text, part-of-speech tag the input text, and lemmatized the input text
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize_and_remove_punctuation(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, removes punctuation from the input text, stems the input text, part-of-speech tag the input text, and lemmatizes the input text, and removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, without punctuation, stems the input text, part-of-speech tag the input text, and lemmatized the input text, and without punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize_and_remove_punctuation("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize_and_remove_punctuation_and_stem(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, removes punctuation from the input text, stems the input text, part-of-speech tag the input text, and lemmatizes the input text, and removes punctuation from the input text, and stems the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, without punctuation, stems the input text, part-of-speech tag the input text, and lemmatized the input text, and without punctuation, and stems the input text
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize_and_remove_punctuation_and_stem("I am running in a race.")
        'i am running in a race'

        """

    def lemmatize_and_remove_stopwords_and_punctuation_and_stem_and_pos_tag_and_lemmatize_and_remove_punctuation_and_stem_and_pos_tag(self, sentence):
        """
        Removes stopwords from the input text, lemmatizes the input text, removes punctuation from the input text, stems the input text, part-of-speech tag the input text, and lemmatizes the input text, and removes punctuation from the input text, and stems the input text, and part-of-speech tag the input text.
        :param sentence: a sentence str
        :return: str, sentence without stopwords, lemmatized, without punctuation, stems the input text, part-of-speech tag the input text, and lemmatized the input text, and without punctuation, and stems the input text, and part-of-speech tag