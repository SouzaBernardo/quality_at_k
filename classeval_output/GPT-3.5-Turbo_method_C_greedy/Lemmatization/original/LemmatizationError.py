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
        # Remove punctuation
        sentence = self.remove_punctuation(sentence)
    
        # Perform part-of-speech tagging
        pos_tags = self.get_pos_tag(sentence)
    
        # Tokenize the sentence
        words = nltk.word_tokenize(sentence)
    
        # Lemmatize each word based on its part-of-speech tag
        lemmatized_words = []
        for word, pos_tag in zip(words, pos_tags):
            if pos_tag.startswith('N'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
            elif pos_tag.startswith('V'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
            elif pos_tag.startswith('R'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
            elif pos_tag.startswith('J'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
            else:
                lemmatized_word = self.lemmatizer.lemmatize(word)
    
            lemmatized_words.append(lemmatized_word)
    
        return lemmatized_words
    

    def get_pos_tag(self, sentence):
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Perform part-of-speech tagging on the tokens
        pos_tags = pos_tag(tokens)
        
        # Extract the part-of-speech tags from the tagged tokens
        pos_tags = [tag[1] for tag in pos_tags]
        
        return pos_tags
    

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        # Get a string of all punctuation characters
        punctuation = string.punctuation
    
        # Initialize an empty string to store the sentence without punctuation
        sentence_without_punctuation = ""
    
        # Iterate through each character in the sentence
        for char in sentence:
            # Check if the character is not a punctuation character
            if char not in punctuation:
                # Append the character to the new string
                sentence_without_punctuation += char
    
        # Return the sentence without punctuation
        return sentence_without_punctuation
    