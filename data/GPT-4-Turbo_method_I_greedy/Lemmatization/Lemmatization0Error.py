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
        # Remove punctuation
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
        # Tokenize the sentence
        tokenized_sentence = word_tokenize(sentence)
    
        # Part of speech tagging
        pos_tagged_sentence = pos_tag(tokenized_sentence)
    
        # Lemmatize words based on their parts of speech
        lemmatized_sentence = []
        for word, tag in pos_tagged_sentence:
            if tag.startswith('N'):
                lemmatized_sentence.append(self.lemmatizer.lemmatize(word, pos='n'))
            elif tag.startswith('V'):
                lemmatized_sentence.append(self.lemmatizer.lemmatize(word, pos='v'))
            elif tag.startswith('R'):
                lemmatized_sentence.append(self.lemmatizer.lemmatize(word, pos='r'))
            else:
                lemmatized_sentence.append(self.lemmatizer.lemmatize(word))
    
        return lemmatized_sentence
    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        # Remove punctuation
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
        # Tokenize the sentence
        tokenized_sentence = word_tokenize(sentence)
    
        # Part of speech tagging
        pos_tagged_sentence = pos_tag(tokenized_sentence)
    
        # Extract the tags and return them
        return [tag for word, tag in pos_tagged_sentence]
    
    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))