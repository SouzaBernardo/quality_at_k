
class NLPDataProcessor:  
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """


    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
        stop_word_list = ['the', 'a', 'an']
        return stop_word_list
