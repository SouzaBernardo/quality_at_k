class Words2Numbers:
    """
    The class provides a text-to-number conversion utility, allowing conversion of written numbers (in words) to their numerical representation.
    """


    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion
        """
        self.numwords = {}
        self.units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]

        self.numwords["and"] = (1, 0)
        for idx, word in enumerate(self.units):
            self.numwords[word] = (1, idx)
        for idx, word in enumerate(self.tens):
            self.numwords[word] = (1, idx * 10)
        for idx, word in enumerate(self.scales):
            self.numwords[word] = (10 ** (idx * 3 or 2), 0)

        self.ordinal_words = {'first': 1,'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]


    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """

    def convert_to_num(self, textnum):
        """
        Convert the word string to the corresponding number string
        :param textnum: string, the word string to be converted
        :return: string, the final converted number string
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_num("thirty-two")
        "32"
        """

    def convert_to_num_list(self, textnum):
        """
        Convert the word string to the corresponding number string list
        :param textnum: string, the word string to be converted
        :return: list, the final converted number string list
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_num_list("thirty-two")
        ['32', '32']
        """

    def convert_to_num_dict(self, textnum):
        """
        Convert the word string to the corresponding number string dictionary
        :param textnum: string, the word string to be converted
        :return: dictionary, the final converted number string dictionary
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_num_dict("thirty-two")
        {'first': '32','second': '32', 'third': '32', 'fifth': '32', 'eighth': '32', 'ninth': '32', 'twelfth': '32'}
        """

    def convert_to_num_list_dict(self, textnum):
        """
        Convert the word string to the corresponding number string list dictionary
        :param textnum: string, the word string to be converted
        :return: dictionary, the final converted number string list dictionary
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_num_list_dict("thirty-two")
        {'first': '32','second': '32', 'third': '32', 'fifth': '32', 'eighth': '32', 'ninth': '32', 'twelfth': '32'}
        """

    def convert_to_num_dict_list(self, textnum):
        """
        Convert the word string to the corresponding number string dictionary list
        :param textnum: string, the word string to be converted
        :return: list, the final converted number string list dictionary
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_num_dict_list("thirty-two")
        ['32', '32']
        """

    def convert_to_num_dict_list_dict(self, textnum):
        """
        Convert the word string to the corresponding number string dictionary list dictionary
        :param textnum: string, the word string to be converted
        :return: dictionary, the final converted number string list dictionary
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_num_dict_list_dict("thirty-two")
        {'first': '32','second': '32', 'third': '32', 'fifth': '32', 'eighth': '32', 'ninth': '32', 'twelfth': '32'}
        """

    def convert_to_num_list_dict_list(self, textnum):
        """
        Convert the word string to the corresponding number string list dictionary list
        :param textnum: string, the word string to be converted
        :return: list, the final converted number string list dictionary list
        >>> w2n = Words