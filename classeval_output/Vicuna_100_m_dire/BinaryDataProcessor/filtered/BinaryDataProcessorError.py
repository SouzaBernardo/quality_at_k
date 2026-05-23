class BinaryDataProcessor: 
    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()



    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non 0 or 1 characters.
        """
        self.binary_string = "".join(filter(lambda x: x == 0 or x == 1, self.binary_string))

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        binary_string = self.binary_string
        zeroes = 0
        ones = 0
        bit_length = 0
        for char in binary_string:
            if char == '0':
                zeroes += 1
            elif char == '1':
                ones += 1
            else:
                break
        bit_length = len(binary_string)
        self.calculate_info(zeroes, ones, bit_length)


    def convert_to_ascii(self):
        binary_string = self.binary_string
        ascii_string = ""
        for i in range(len(binary_string)):
            if binary_string[i] == "0":
                ascii_string += "0"
            else:
                ascii_string += "1"
        return ascii_string

    def convert_to_utf8(self):
        binary_string = self.binary_string
        binary_string = binary_string.translate(str.maketrans('', '', string.punctuation))
        binary_string = binary_string.encode('utf-8')
        return binary_string