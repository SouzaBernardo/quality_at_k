
class BinaryDataProcessor: 
    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()





    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        zeroes = self.binary_string.count('0')
        ones = self.binary_string.count('1')
        total_length = len(self.binary_string)
        return {'Zeroes': zeroes / total_length, 'Ones': ones / total_length, 'Bit length': total_length}

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        # create an empty string
        ascii_string = ""
        # loop through the binary string
        for i in range(0, len(self.binary_string), 7):
            # get the next 7 characters in the string
            chars = self.binary_string[i:i+7]
            # convert each character to its corresponding ascii character
            ascii_char = chr(int(chars, 2))
            # add the ascii character to the string
            ascii_string += ascii_char
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        # convert the binary string to a list of bytes
        binary_list = [self.binary_string[i:i+8] for i in range(0, len(self.binary_string), 8)]
        # convert each byte to an ascii character
        ascii_list = [chr(int(binary_list[i], 2)) for i in range(len(binary_list))]
        # convert the ascii list to a utf-8 string
        utf8_string = ''.join(ascii_list)
        return utf8_string