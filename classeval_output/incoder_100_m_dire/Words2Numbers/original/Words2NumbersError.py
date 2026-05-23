
class Words2Numbers: 
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
        tens = [word for word in intwords if word in self.tens]
        scales = [word for word in intwords if word in self.scales]
        scalewords = [word for word in scales if word in self.numwords]
        scalehundreds = [word for word in scalewords if word[0].isdigit()]
        scalethousands = [word for word in scalewords if word[0].isdigit() and word[1].isdigit()]
        scalemillions = [word for word in scalewords if word[0].isdigit() and word[1].isdigit() and word[2].isdigit()]
        scalebillions = [word for word in scalewords if word[0].isdigit() and word[1].isdigit() and word[2].isdigit() and word[3].isdigit()]
        scaletrillions = [word for word in scalewords if word[0].isdigit() and word[1].isdigit() and word[2].isdigit() and word[3].isdigit() and word[4].isdigit()]

        intwords = [word for word in intwords if word not in self.ordinal_words]
        intwords = [word for word in intwords if word not in self.ordinal_endings]

        if len(intwords) == 0:
            return textnum
        elif len(intwords) == 1:
            return intwords[0]
        else:
            intwords.sort()
            intwords.reverse()
            intwords.insert(0, intwords.pop())
            intwords.insert(0, scalehundreds.pop())
            intwords.insert(0, scalethousands.pop())
            intwords.insert(0, scalemillions.pop())
            intwords.insert(0, scalebillions.pop())
            intwords.insert(0, scaletrillions.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, tens.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            intwords.insert(0, scalewords.pop())
            return intword


    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        words = textnum.split()
        for word in words:
            if word not in self.numwords:
                return False
        return True
