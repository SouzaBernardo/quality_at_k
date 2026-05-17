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
        return True


    def convert_to_numbers(self, textnum):
        """
        Convert the word string to the corresponding numerical string
        :param textnum: string, the word string to be converted
        :return: string, the final converted numerical string
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_numbers("thirty-two")
        "32"
        """
        return self.numwords[textnum]


    def convert_to_words(self, textnum):
        """
        Convert the word string to the corresponding words
        :param textnum: string, the word string to be converted
        :return: string, the final converted words
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_words("thirty-two")
        "thirty-two"
        """
        return self.numwords[textnum]


    def convert_to_ordinal(self, textnum):
        """
        Convert the word string to the corresponding ordinal string
        :param textnum: string, the word string to be converted
        :return: string, the final converted ordinal string
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_ordinal("thirty-two")
        "thirty-two"
        """
        return self.numwords[textnum]


    def convert_to_tens(self, textnum):
        """
        Convert the word string to the corresponding tens
        :param textnum: string, the word string to be converted
        :return: string, the final converted tens
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_tens("thirty-two")
        "thirty-two"
        """
        return self.numwords[textnum]


    def convert_to_scales(self, textnum):
        """
        Convert the word string to the corresponding scales
        :param textnum: string, the word string to be converted
        :return: string, the final converted scales
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_scales("thirty-two")
        "thirty-two"
        """
        return self.numwords[textnum]


    def convert_to_ordinal_endings(self, textnum):
        """
        Convert the word string to the corresponding ordinal ending
        :param textnum: string, the word string to be converted
        :return: string, the final converted ordinal ending
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_ordinal_endings("thirty-two")
        "thirty-two"
        """
        return self.numwords[textnum]


    def convert_to_ordinal_words(self, textnum):
        """
        Convert the word string to the corresponding ordinal words
        :param textnum: string, the word string to be converted
        :return: string, the final converted ordinal words
        >>> w2n = Words2Numbers()
        >>> w2n.convert_to_ordinal_words("thirty-two")
        "thirty-two"
        """
        return self