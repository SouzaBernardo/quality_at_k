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
        """
        # Remove punctuations from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        # Tag the parts of speech of each word
        tagged_tokens = pos_tag(tokens)
        # Lemmatize each word with the appropriate parameters based on its part of speech
        lemmatized_tokens = [self.lemmatizer.lemmatize(token, pos=tag) for token, tag in tagged_tokens]
        return lemmatized_tokens

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        # Remove punctuations from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        # Tag the parts of speech of each word
        tagged_tokens = pos_tag(tokens)
        # Extract the part of speech tag of each word
        pos_tags = [tag for token, tag in tagged_tokens]
        return pos_tags

