
class NLPDataProcessor:  
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """





    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        """
        processed_list = []
        for string in string_list:
            words = string.split()
            for word in words:
                if word.lower() not in stop_word_list:
                    processed_list.append(word)
        return processed_list

