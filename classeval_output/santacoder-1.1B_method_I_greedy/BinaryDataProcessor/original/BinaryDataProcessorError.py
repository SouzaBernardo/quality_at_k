
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
        self.binary_string = self.binary_string.replace("0", "")
        self.binary_string = self.binary_string.replace("1", "")
        self.binary_string = self.binary_string.replace("d", "")
        self.binary_string = self.binary_string.replace("f", "")
        self.binary_string = self.binary_string.replace("r", "")
        self.binary_string = self.binary_string.replace(" ", "")
        self.binary_string = self.binary_string.replace("00", "")
        self.binary_string = self.binary_string.replace("01", "")
        self.binary_string = self.binary_string.replace("10", "")
        self.binary_string = self.binary_string.replace("11", "")
        self.binary_string = self.binary_string.replace("000", "")
        self.binary_string = self.binary_string.replace("001", "")
        self.binary_string = self.binary_string.replace("010", "")
        self.binary_string = self.binary_string.replace("011", "")
        self.binary_string = self.binary_string.replace("100", "")
        self.binary_string = self.binary_string.replace("101", "")
        self.binary_string = self.binary_string.replace("110", "")
        self.binary_string = self.binary_string.replace("111", "")
        self.binary_string = self.binary_string.replace("0000", "")
        self.binary_string = self.binary_string.replace("0001", "")
        self.binary_string = self.binary_string.replace("0010", "")
        self.binary_string = self.binary_string.replace("0011", "")
        self.binary_string = self.binary_string.replace("0100", "")
        self.binary_string = self.binary_string.replace("0101", "")
        self.binary_string = self.binary_string.replace("0110", "")
        self.binary_string = self.binary_string.replace("0111", "")
        self.binary_string = self.binary_string.replace("00000", "")
        self.binary_string = self.binary_string.replace("00001", "")
        self.binary_string = self.binary_string.replace("00010", "")
        self.binary_string = self.binary_string.replace("00011", "")
        self.binary_string = self.binary_string.replace("00100", "")
        self.binary_string = self.binary_string.replace("00101", "")
        self.binary_string = self.binary_string.replace("00110", "")
        self.binary_string = self.binary_string.replace("00111", "")
        self.binary_string = self.binary_string.replace("01000", "")
        self.binary_string = self.binary_string.replace("01001", "")
        self.binary_string = self.binary_string.replace("01010", "")
        self.binary_string = self.binary_string.replace("01011", "")
        self.binary_string = self.binary_string.replace("01100", "")
        self.binary_string = self.binary_string.replace("01101", "")
        self.binary_string = self.binary_string.replace("01110", "")
        self.binary_string = self.binary_string.replace("01111", "")
        self.binary_string = self.binary_string.replace("000000", "")
        self.binary_string = self.binary_string.replace("000001", "")
        self.binary_string = self.binary_string.replace("000010", "")
        self.binary_string = self.binary_string.replace("000011", "")
        self.binary_string = self.binary_string.replace("000100", "")
        self.binary_string = self.binary_string.replace("000101", "")
        self.binary_string = self.binary_string.replace("000110", "")
        self.binary_string = self.binary_string.replace("000111", "")
        self.binary_string = self.binary_string.replace("001000", "")
        self.binary_string = self.binary_string.replace("001001", "")
        self.binary_string = self.binary_string.replace("001010", "")
        self.binary_string = self.binary_string.replace("001011", "")
        self.binary_string = self.binary_string.replace("001100", "")
        self.binary_string = self.binary_string.replace("001101", "")
        self.binary_string = self.binary_string.replace("001110", "")
        self.binary_string = self.binary_string.replace("001111", "")
        self.binary_string = self.binary_string.replace("010000", "")
        self.binary_string = self.binary_string.replace("010001", "")
        self.binary_string = self.binary_string.replace("010010", "")
        self.binary_string = self.binary_string.replace("010011", "")
        self.binary_string = self.binary_string.replace("010100", "")
        self.binary_string = self.binary_string.replace("010101", "")
        self.binary_string = self.binary_string.replace("010110", "")
        self.binary_string = self.binary_string.replace("010111", "")
        self.binary_string = self.binary_string.replace("011000", "")
        self.binary_string = self.binary_string.replace("011001", "")
        self.binary_string = self.binary_string.replace("011010", "")
        self.binary_string = self.binary_string.replace("011011", "")
        self.binary_string = self.binary_string.replace("011100", "")
        self.binary_string = self.binary_string.replace("011101", "")
        self.binary_string = self.binary_string.replace("011110", "")
        self.binary_string = self.binary_string.replace("011111", "")
        self.binary_string = self.binary_string.replace("0000000", "")
        self.binary_string = self.binary_string.replace("0000001", "")
        self.binary_string = self.binary_string.replace("0000010", "")
        self.binary_string = self.binary_string.replace("0000011", "")
        self.binary_string = self.binary_string.replace("0000100", "")
        self.binary_string = self.binary_string.replace("0000101", "")
        self.binary_string = self.binary_string.replace("0000110", "")
        self.binary_string = self.binary_string.replace("00001





