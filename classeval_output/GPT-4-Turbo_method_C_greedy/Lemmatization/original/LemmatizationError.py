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
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']
        """
        sentence = self.remove_punctuation(sentence)
        pos_tagged_sentence = self.get_pos_tag(sentence)
        lemmatized_sentence = []
        for word, tag in pos_tagged_sentence:
            if tag.startswith('N'):
                pos = 'n'
            elif tag.startswith('V'):
                pos = 'v'
            else:
                pos = 'a'
            lemmatized_word = self.lemmatizer.lemmatize(word, pos)
            lemmatized_sentence.append(lemmatized_word)
        return lemmatized_sentence
    
    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        # Remove punctuation
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokenized_sentence = word_tokenize(sentence)
        
        # Get the part of speech tag for each word
        pos_tags = pos_tag(tokenized_sentence)
        
        # Return only the tags, not the words
        return [tag for word, tag in pos_tags]
    
    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        return sentence.translate(str.maketrans('', '', string.punctuation))
