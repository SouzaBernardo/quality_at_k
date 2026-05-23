
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
        >>> bdp = BinaryDataProcessor("01101000daf3e4r01100101011011000110110001101111")
        >>> bdp.clean_non_binary_chars()
        >>> bdp.binary_string
        '0110100001100101011011000110110001101111'

        """
        return ''.join([c for c in self.binary_string if c.isdigit() or c.islower()])

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        zero_one_ratio = (self.binary_string[0] == '0') * 100.0 / (self.binary_string[1] == '1') * 100.0
        total_length = len(self.binary_string)
        binary_info = {'Zeroes': zero_one_ratio * total_length, 'Ones': zero_one_ratio * (total_length - 1) * 100.0}
        return binary_info

    def convert_to_ascii(self):
        """
        Convert the binary string to ASCII string.
        """
        return self.binary_string.replace('0', '').replace('1', '').encode('ascii')