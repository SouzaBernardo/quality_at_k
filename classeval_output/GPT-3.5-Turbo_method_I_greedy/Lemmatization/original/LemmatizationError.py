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
        # Remove punctuations from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_words = pos_tag(words)
        
        # Lemmatize the words based on their parts of speech
        lemmatized_words = []
        for word, tag in tagged_words:
            if tag.startswith('NN'):  # Noun
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='n'))
            elif tag.startswith('VB'):  # Verb
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='v'))
            elif tag.startswith('JJ'):  # Adjective
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='a'))
            elif tag.startswith('R'):  # Adverb
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos='r'))
            else:
                lemmatized_words.append(word)
        
        return lemmatized_words
    

    def get_pos_tag(self, sentence):
        # Remove punctuations from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_words = pos_tag(words)
        
        # Extract only the part of speech tags
        pos_tags = [tag for _, tag in tagged_words]
        
        return pos_tags
    

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        return sentence
    