
class NLPDataProcessor: 


    def construct_stop_word_list(self):
        stop_word_list = ['a', 'an', 'the']
        return stop_word_list

    def remove_stop_words(string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
    
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
    
        stop_word_list = stop_word_list.split(',')
        filtered_string_list = []
        for word in string_list:
            filtered_word = word.lower()
            for stop_word in stop_word_list:
                if filtered_word.startswith(stop_word):
                    filtered_string_list.append(' '.join(filtered_word.split()))
                    break
        return filtered_string_list

    def process(self, string_list):
        stop_word_list = set(stop_words)
        processed_string_list = []
        for string in string_list:
            words = string.split()
            for word in words:
                if word not in stop_word_list:
                    processed_string_list.append(word)
        return processed_string_list