
class BinaryDataProcessor:  
    """
    This is a class used to process binary data, which includes functions such as clearing non 0 or 1 characters, counting binary string information, and converting to corresponding strings based on different encoding methods.
    """

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
        """
        self.clean_non_binary_chars()
        zeroes = 0
        ones = 0
        bit_length = 0
        for char in self.binary_string:
            if char == '0':
                zeroes += 1
            elif char == '1':
                ones += 1
        total_chars = len(self.binary_string)
        binary_info = {'Zeroes': zeroes/total_chars*100, 'Ones': ones/total_chars*100, 'Bit length': total_chars}
        return binary_info

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        binary_info = self.calculate_binary_info()
        ascii_string = ""
        for i in range(0, len(self.binary_string), 2):
            ascii_string += chr(int(self.binary_string[i], 2) * 256 + int(self.binary_string[i+1], 2))
        return ascii_string

    def convert_to_utf8(self):
        binary_info = self.calculate_binary_info()
        ascii_string = self.convert_to_ascii()
        utf8_string = unicodedata.normalize('NFKD', ascii_string).encode('ascii', 'ignore').decode('utf-8')
        return utf8_string