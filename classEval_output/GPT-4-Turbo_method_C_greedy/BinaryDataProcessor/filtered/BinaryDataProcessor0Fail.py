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
        self.binary_string = ''.join(char for char in self.binary_string if char in '01')
    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        total_length = len(self.binary_string)
        ones = self.binary_string.count('1')
        zeroes = self.binary_string.count('0')

        return {
            'Zeroes': round(zeroes / total_length, 3),
            'Ones': round(ones / total_length, 3),
            'Bit length': total_length
        }

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'
        """
        binary_values = [self.binary_string[i:i+8] for i in range(0, len(self.binary_string), 8)]
        ascii_string = ''.join([chr(int(binary, 2)) for binary in binary_values])
        return ascii_string
    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_utf8()
        'hello'
        """
        n = int(self.binary_string, 2)
        byte_number = (n.bit_length() + 7) // 8
    
        binary_array = bytearray()
    
        for _ in range(byte_number):
            binary_array.append(n & 0xff)
            n = n >> 8
        binary_array.reverse()
    
        return binary_array.decode('utf8')