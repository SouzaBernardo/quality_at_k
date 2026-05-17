class NLPDataProcessor: 


    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
        return ['a', 'an', 'the']




    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        return [x for x in string_list if x not in stop_word_list]




    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        stop_word_list = []
        for string in string_list:
            stop_word = string.split(' ')
            if len(stop_word) == 1:
                stop_word_list.append(stop_word[0])
            else:
                stop_word_list.append(stop_word[0])
                stop_word_list.append(stop_word[1])
                stop_word_list.append(stop_word[2])
                stop_word_list.append(stop_word[3])
                stop_word_list.append(stop_word[4])
                stop_word_list.append(stop_word[5])
                stop_word_list.append(stop_word[6])
                stop_word_list.append(stop_word[7])
                stop_word_list.append(stop_word[8])
                stop_word_list.append(stop_word[9])
                stop_word_list.append(stop_word[10])
                stop_word_list.append(stop_word[11])
                stop_word_list.append(stop_word[12])
                stop_word_list.append(stop_word[13])
                stop_word_list.append(stop_word[14])
                stop_word_list.append(stop_word[15])
                stop_word_list.append(stop_word[16])
                stop_word_list.append(stop_word[17])
                stop_word_list.append(stop_word[18])
                stop_word_list.append(stop_word[19])
                stop_word_list.append(stop_word[20])
                stop_word_list.append(stop_word[21])
                stop_word_list.append(stop_word[22])
                stop_word_list.append(stop_word[23])
                stop_word_list.append(stop_word[24])
                stop_word_list.append(stop_word[25])
                stop_word_list.append(stop_word[26])
                stop_word_list.append(stop_word[27])
                stop_word_list.append(stop_word[28])
                stop_word_list.append(stop_word[29])
                stop_word_list.append(stop_word[30])
                stop_word_list.append(stop_word[31])
                stop_word_list.append(stop_word[32])
                stop_word_list.append(stop_word[33])
                stop_word_list.append(stop_word[34])
                stop_word_list.append(stop_word[35])
                stop_word_list.append(stop_word[36])
                stop_word_list.append(stop_word[37])
                stop_word_list.append(stop_word[38])
                stop_word_list.append(stop_word[39])
                stop_word_list.append(stop_word[40])
                stop_word_list.append(stop_word[41])
                stop_word_list.append(stop_word[42])
                stop_word_list.append(stop_word[43])
                stop_word_list.append(stop_word[44])
                stop_word_list.append(stop_word[45])
                stop_word_list.append(stop_word[46])
                stop_word_list.append(stop_word[47])
                stop_word_list.append(stop_word[48])
                stop_word_list.append(stop_word[49])
                stop_word_list.append(stop_word[50])
                stop_word_list.append(stop_word[51])
                stop_word_list.append(stop_word[52])
                stop_word_list.append(stop_word[53])
                stop_word_list.append(stop_word[54])
                stop_word_list.append(stop_word[55])