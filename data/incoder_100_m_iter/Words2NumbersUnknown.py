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

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
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
        intwords = [word for word in textnum.split() if word in self.numwords]
        tens = [word for word in intwords if word in self.numwords]
        scales = [word for word in intwords if word in self.scales]
        numwords = [word for word in intwords if word in self.units]
        intnum = ""
        negative = False
        if intwords[0][0] == '-':
            negative = True
            intwords = intwords[1:]
        for word in intwords:
            if word in self.numwords:
                scale, idx = self.numwords[word]
                intnum += str(int(word) * scale + idx)
            elif word in self.scales:
                scale, idx = self.scales.index(word), 0
                intnum += str(int(word) * scale + idx)
            elif word in self.units:
                scale, idx = self.units.index(word), 0
                intnum += str(int(word) * scale + idx)
            elif word in self.tens:
                scale, idx = self.tens.index(word), 0
                intnum += str(int(word) * scale + idx)
            elif word in self.ordinal_words:
                scale, idx = self.ordinal_words[word], 0
                intnum += str(int(word) * scale + idx)
            elif word.isdigit():
                intnum += word
            else:
                intnum += self.text2int(word)
        if intnum.endswith(".0"):
            intnum = intnum[:-2]
        if negative:
            intnum = "-" + intnum
        return intnum


    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        intwords = [word for word in textnum.split() if word in self.numwords]
        tens = [word for word in intwords if word in self.numwords]
        scales = [word for word in intwords if word in self.scales]
        numwords = [word for word in intwords if word in self.units]
        intnum = ""
        negative = False
        if intwords[0][0] == '-':
            negative = True
            intwords = intwords[1:]
        for word in intwords:
            if word in self.numwords:
                scale, idx = self.numwords[word]
                intnum += str(int(word) * scale + idx)
            elif word in self.scales:
                scale, idx = self.scales.index(word), 0
                intnum += str(int(word) * scale + idx)
            elif word in self.units:
                scale, idx = self.units.index(word), 0
                intnum += str(int(word) * scale + idx)
            elif word in self.tens:
                scale, idx = self.tens.index(word), 0
                intnum += str(int(word) * scale + idx)
            elif word in self.ordinal_words:
                scale, idx = self.ordinal_words[word], 0
                intnum += str(int(word) * scale + idx)
            elif word.isdigit():
                intnum += word
            else:
                return False
        if intnum.endswith(".0"):
            intnum = intnum[:-2]
        if negative:
            intnum = "-" + intnum
        return True