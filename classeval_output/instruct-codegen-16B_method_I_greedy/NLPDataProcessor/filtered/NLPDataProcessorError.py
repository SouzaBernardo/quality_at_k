class NLPDataProcessor:  
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """



    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
        return ['a', 'an', 'the']

    def remove_stop_words(self, string_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        """
        words = []
        for string in string_list:
            words += self.process(string)
        return words

    def process(self, string):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string: a string
        :return: a list of words without stop words
        """
        words = string.split()
        filtered_words = [word for word in words if word not in self.stop_words]
        return filtered_words