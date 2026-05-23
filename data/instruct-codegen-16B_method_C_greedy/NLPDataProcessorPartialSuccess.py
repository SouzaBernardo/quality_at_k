class NLPDataProcessor: 


    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
        stop_words = ['a', 'an', 'the']
        return stop_words

    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        """
        words = []
        for string in string_list:
            word_list = string.split()
            for word in word_list:
                if word not in stop_word_list:
                    words.append(word)
        return words

    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        """
        stop_word_list = ['a', 'an', 'the']
        return [word for word in string_list if word not in stop_word_list]