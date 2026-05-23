Here is the completed `SplitSentence` class:
```python
import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        """
        sentences = re.findall(r'\b\w+(?:\.\w+)*\b', sentences_string)
        return sentences

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        """
        words = len(sentence.split())
        return words

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        """
        sentences = sentences_string.split()
        longest_sentence = max(sentences, key=len)
        return len(longest_sentence.split())
```
This class uses regular expressions to split the input sentence into a list of words, and then uses the `max` function to find the longest sentence in the list. The `count_words` method counts the number of words in the sentence, and the `process_text_file` method processes the input text and returns the number of words in the longest sentence.