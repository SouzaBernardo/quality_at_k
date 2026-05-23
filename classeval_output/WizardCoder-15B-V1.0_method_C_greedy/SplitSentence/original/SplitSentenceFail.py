import re
class SplitSentence: 


    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with. or? and with a space after that. Please note that Mr. also end with. but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        # Remove Mr. from the beginning of the sentence
        sentences_string = re.sub(r'^Mr\. ', '', sentences_string, flags=re.IGNORECASE)
        # Split the string into sentences using regular expressions
        sentences = re.split(r'(?<=[.?!])\s', sentences_string)
        # Remove empty strings from the list
        sentences = list(filter(None, sentences))
        return sentences

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        """
        # Split the sentence into words using the regular expression \w+
        words = re.findall(r'\w+', sentence)
        # Filter out any punctuation marks and numbers
        words = [word for word in words if word.isalpha()]
        # Return the length of the resulting list as the number of words in the sentence
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        """
        # Split the text into sentences
        sentences = re.split(r'[.?!]', sentences_string)
        # Find the longest sentence
        longest_sentence = ""
        for sentence in sentences:
            if len(sentence.split()) > len(longest_sentence.split()):
                longest_sentence = sentence
        # Count the number of words in the longest sentence
        return len(longest_sentence.split())