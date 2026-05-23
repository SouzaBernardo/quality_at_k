
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
        """
        # Split the textnum into individual words
        words = textnum.split()
    
        # Initialize variables for the final integer and the current scale
        current = result = 0
        scale = 1
    
        # Iterate through each word in the textnum
        for word in words:
            # Check if the word is an ordinal word
            if word in self.ordinal_words:
                # Add the corresponding ordinal number to the result
                result += self.ordinal_words[word]
            # Check if the word is a number word
            elif word in self.numwords:
                # Get the scale and value of the word
                scale, increment = self.numwords[word]
                # Update the current value based on the scale and increment
                current = current * scale + increment
                # Check if the current scale is greater than or equal to 1000
                if scale >= 1000:
                    # Add the current value to the result and reset the current value
                    result += current
                    current = 0
            else:
                # Handle cases where the word is not recognized
                raise ValueError("Invalid word: " + word)
    
        # Add the remaining current value to the result
        result += current
    
        # Return the final converted integer as a string
        return str(result)
    

    def is_valid_input(self, textnum):
        try:
            self.text2int(textnum)
            return True
        except ValueError:
            return False
    