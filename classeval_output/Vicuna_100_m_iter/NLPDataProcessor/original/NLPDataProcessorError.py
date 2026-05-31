
class NLPDataProcessor:  
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """



    def construct_stop_word_list(self):
        stop_words = set()
        stop_words.add('a')
        stop_words.add('an')
        stop_words.add('the')
        return list(stop_words)

    def remove_stop_words(self, string_list, stop_word_list):
        stop_words = set()
        for word in string_list:
            stop_words.add(word)
        filtered_list = [word for word in string_list if word not in stop_words]
        return filtered_list

    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        ['This', 'is', 'test.']
        """