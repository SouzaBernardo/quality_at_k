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
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.clean_non_binary_chars()
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'

        """
        binary_string = self.binary_string
        binary_string = binary_string.replace('0', '')
        binary_string = binary_string.replace('1', '')
        self.binary_string = binary_string


    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        bit_length = len(self.binary_string)
        zeroes = bit_length / self.binary_string.count("0")
        ones = bit_length / self.binary_string.count("1")
        return {'Zeroes': zeroes, 'Ones': ones, 'Bit length': bit_length}


    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'

        """
        ascii_string = ""
        for char in self.binary_string:
            if char == "1":
                ascii_string += "a"
            elif char == "0":
                ascii_string += "0"
            else:
                ascii_string += char
        return ascii_string


    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_utf8()
        'hello'

        """
        utf8_string = str(self.binary_string, 'utf-8')
        return utf8_string