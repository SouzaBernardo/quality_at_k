
class NLPDataProcessor:  
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """



    def construct_stop_word_list(self):
        stop_words = ['a', 'an', 'the']
        return [word for word in stop_words if word not in self._stop_words]

    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        self._stop_words = set(stop_word_list)
        return [word for word in string_list if word not in self._stop_words]

    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        return self.process_strings(string_list)
