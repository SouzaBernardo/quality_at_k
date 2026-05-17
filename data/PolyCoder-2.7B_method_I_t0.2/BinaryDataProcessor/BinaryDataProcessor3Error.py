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
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.binary_string.replace("0", "1")
        self.binary_string = self.binary_string.replace("1", "0")
        self.binary_string = self.