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
        self.binary_string = ''.join(char for char in self.binary_string if char in '01')
    
    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        total_length = len(self.binary_string)
        ones = self.binary_string.count('1')
        zeroes = self.binary_string.count('0')
    
        return {'Zeroes': zeroes / total_length, 'Ones': ones / total_length, 'Bit length': total_length}
    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        binary_int = int(self.binary_string, 2)
        byte_number = binary_int.bit_length() + 7 // 8
    
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
    
        return ascii_text
    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        binary_int = int(self.binary_string, 2)
        byte_number = binary_int.bit_length() + 7 // 8
    
        binary_array = binary_int.to_bytes(byte_number, "big")
        utf8_text = binary_array.decode('utf-8')
    
        return utf8_text