Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class LongestWord in the following code.
import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []

    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """

### Response:Here's the completed code for the `LongestWord` class:

```python
import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []

    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        """
        # remove punctuation marks
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        # split sentence into a list of word
        word_list = sentence.split()
        # find the longest word in the word_list that is in the self.word_list
        longest_word = ''
        for word in word_list:
            if word.lower() in [w.lower() for w in self.word_list]:
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
```

The `add_word` method simply appends the input word to the `word_list` attribute. The `find_longest_word` method first removes all punctuation marks from the input sentence using the `translate` method and the `string.punctuation` constant. It then splits the sentence into a list of words using the `split` method. Finally, it iterates over the list of words and checks if each word is in the `word_list` attribute (case-insensitive). If a word is found, it checks if its length is greater than the length of the current longest word. If it is, it updates the `longest_word` variable. Finally, it returns the `longest_word` variable. If the `word_list` attribute is empty, it returns an empty string.