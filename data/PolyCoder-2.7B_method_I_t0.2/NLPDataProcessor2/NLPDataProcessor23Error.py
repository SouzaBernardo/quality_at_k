from collections import Counter
import re
class NLPDataProcessor2:  
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """



    def process_data(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        >>> NLPDataProcessor.process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
        words_list = []
        for string in string_list:
            string = string.lower()
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r'[^\s\w\s]', '', string)
            string = re.sub(r'[^\w\s]', '', string)
            string = re.sub(r