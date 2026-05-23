import nltk
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
        punctuations = set(string.punctuation)
        sentence = sentence.lower()
        words = sentence.split()
        lemmatizer = WordNetLemmatizer()
        pos_tags = pos_tag(words)
        for word in words:
            if word not in punctuations:
                lemmatizer.lemmatize(word, 'en')
                pos_tags[word] = 'pos_' + word
        return [word for word, tag in pos_tags.items() if tag!= 'pos_']

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        punctuations = sentence.splitpunctuation()
        sentence = sentence.replace(punctuations, '')
        sentence = pos_tag.apply(sentence, pos_tag.split())
        sentence = word_tokenize(sentence)
        return [pos_tag.apply(word, pos_tag.split()) for word in sentence]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        # Remove punctuation from sentence
        sentence = sentence.replace(".", "") #. to remove
        sentence = sentence.replace(", ", "") #, to remove
        sentence = sentence.replace(" ", "") # space to remove
        sentence = sentence.replace(" ", ".") # space and period to remove
        sentence = sentence.replace(" ", ". ") # space and period and space to remove
        sentence = sentence.replace(" ", ". ") # space and period and space and space to remove
        # Convert sentence to lowercase
        sentence = sentence.lower()
        return sentence