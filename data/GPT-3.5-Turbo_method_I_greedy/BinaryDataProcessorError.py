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
        self.binary_string = re.sub("[^01]", "", self.binary_string)


    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        zeroes_count = self.binary_string.count('0')
        ones_count = self.binary_string.count('1')
        total_length = len(self.binary_string)
        
        zeroes_percentage = zeroes_count / total_length
        ones_percentage = ones_count / total_length
        
        binary_info = {
            'Zeroes': zeroes_percentage,
            'Ones': ones_percentage,
            'Bit length': total_length
        }
        
        return binary_info
    

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        ascii_string = ""
        for i in range(0, len(self.binary_string), 8):
            binary_substring = self.binary_string[i:i+8]
            decimal_value = int(binary_substring, 2)
            ascii_character = chr(decimal_value)
            ascii_string += ascii_character
        return ascii_string
    

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        binary_bytes = bytes([int(self.binary_string[i:i+8], 2) for i in range(0, len(self.binary_string), 8)])
        utf8_string = binary_bytes.decode('utf-8')
        return utf8_string