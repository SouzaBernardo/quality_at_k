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
        # Remove punctuations of the sentence
        sentence = sentence.replace("'","").replace('"','').replace('`','').replace('[','').replace(']','').replace('{','').replace('}','')
        # Tokenize the input sentence
        words = word_tokenize(sentence)
        # Mark the part of speech tag of each word
        tags = pos_tag(words)
        # Lemmatize the words with different parameters based on their parts of speech
        lemmatized_words = []
        for tag in tags:
            if tag.startswith('NN'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[2:], pos='n'))
            elif tag.startswith('VB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[2:], pos='v'))
            elif tag.startswith('JJ'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[2:], pos='a'))
            elif tag.startswith('RB'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[2:], pos='d'))
            elif tag.startswith('IN'):
                lemmatized_words.append(self.lemmatizer.lemmatize(tag[2:], pos='a'))
            else:
                lemmatized_words.append(tag)
        return lemmatized_words

    def get_pos_tag(self, sentence):
        # Remove punctuations of the sentence
        sentence = sentence.translate(str.maketrans("", "", string.punctuation))
        # Tokenize the input sentence
        words = word_tokenize(sentence)
        # Lemmatize each word
        lemmas = [self.lemmatizer.lemmatize(word) for word in words]
        # Get the part of speech tag of each word
        pos_tags = [pos_tag(word) for word in lemmas]
        return pos_tags

    def remove_punctuation(self, sentence):
        # Create a list of all punctuation characters
        punctuation = "!@#$%^&*()_+{}:"
        # Split the sentence into a list of words
        words = sentence.split()
        # Initialize an empty string to store the non-punctuated sentence
        non_punctuated_sentence = ""
        # Iterate through the list of words
        for word in words:
            # Check if the current word contains any punctuation characters
            if word.lower() in punctuation:
                # Remove the punctuation from the word
                non_punctuated_sentence += word.replace(punctuation, "")
            else:
                # Add the word to the non-punctuated sentence without any changes
                non_punctuated_sentence += word
        return non_punctuated_sentence