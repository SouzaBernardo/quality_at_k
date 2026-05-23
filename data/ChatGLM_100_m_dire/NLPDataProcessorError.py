class NLPDataProcessor: 


    def construct_stop_word_list(self):
        stop_words = ['a', 'an', 'the']
        string_list = [word for word in self.stop_word_list if word not in string_list]
        return string_list + stop_words

    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        words = []
        for word in string_list:
            if word not in stop_word_list:
                words.append(word)
        return words

    def process(self, string_list):
        stop_words = ['a', 'an', 'the']
        string_list = [word for word in string_list if word not in stop_words]
        return string_list