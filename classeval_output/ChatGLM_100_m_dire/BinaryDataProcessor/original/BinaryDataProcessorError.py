
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
        return ''.join([c for c in self.binary_string if c.isdigit() or c.islower()])

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """
        binary_string = self.binary_string
        zero_count = 0
        one_count = 0
        bit_length = 0
        for char in binary_string:
            if char.is_zero():
                zero_count += 1
            elif char.is_one():
                one_count += 1
            else:
                bit_length += 1
        binary_info = {
            'Zeroes': zero_count / (100.0 * one_count),
            'Ones': one_count / (100.0 * one_count),
            'Bit length': bit_length / (100.0 * one_count)
        }
        return binary_info

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'

        """
        return self.clean_non_binary_chars() + self.calculate_binary_info() + self.convert_to_utf8()

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        Convert the binary string to utf-8 string.
        """
        utf8_string = self.binary_string.encode('utf-8')
        return utf8_string