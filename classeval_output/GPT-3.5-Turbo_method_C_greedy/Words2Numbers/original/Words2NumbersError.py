
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
        """
        # Split the textnum into individual words
        words = textnum.split()
    
        # Initialize variables for the final integer and the current scale
        current = result = 0
        scale = 1
    
        # Iterate through each word in the textnum
        for word in words:
            # Check if the word is a valid input
            if not self.is_valid_input(word):
                return "Invalid input"
    
            # Check if the word is a scale word (e.g. hundred, thousand, million)
            if word in self.scales:
                # Multiply the current value by the scale and add it to the result
                result += current * self.numwords[word][0]
                # Reset the current value
                current = 0
                # Update the scale
                scale = self.numwords[word][0]
            # Check if the word is a unit or ten word
            elif word in self.units or word in self.tens:
                # Add the value of the word to the current value
                current += self.numwords[word][1]
            # Check if the word is an ordinal word
            elif word in self.ordinal_words:
                # Add the value of the ordinal word to the result
                result += self.ordinal_words[word]
            # Check if the word ends with a valid ordinal ending
            elif any(word.endswith(ending[0]) for ending in self.ordinal_endings):
                # Remove the ordinal ending from the word
                for ending in self.ordinal_endings:
                    if word.endswith(ending[0]):
                        word = word[:-len(ending[0])] + ending[1]
                        break
                # Add the value of the word to the result
                result += self.numwords[word][1] * scale
    
        # Add the current value to the result
        result += current
    
        # Return the final converted integer string
        return str(result)
    

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        """
        try:
            self.text2int(textnum)
            return True
        except:
            return False
    