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

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.calculate_binary_info()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_ascii()
        'hello'

        """

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_utf8()
        'hello'

        """

    def convert_to_unicode(self):
        """
        Convert the binary string to unicode string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_unicode()
        'hello'

        """

    def convert_to_binary(self):
        """
        Convert the binary string to binary string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_binary()
        '0110100001100101011011000110110001101111'

        """

    def convert_to_hex(self):
        """
        Convert the binary string to hex string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_hex()
        '0110100001100101011011000110110001101111'

        """

    def convert_to_base64(self):
        """
        Convert the binary string to base64 string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_base64()
        '0110100001100101011011000110110001101111'

        """

    def convert_to_base64_url(self):
        """
        Convert the binary string to base64 url string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_base64_url()
        'http://www.example.com/0110100001100101011011000110110001101111'

        """

    def convert_to_base64_url_with_spaces(self):
        """
        Convert the binary string to base64 url string with spaces.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_base64_url_with_spaces()
        'http://www.example.com/0110100001100101011011000110110001101111'

        """

    def convert_to_base64_url_with_spaces_and_spaces(self):
        """
        Convert the binary string to base64 url string with spaces and spaces.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_base64_url_with_spaces_and_spaces()
        'http://www.example.com/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111'

        """

    def convert_to_base64_url_with_spaces_and_spaces_and_spaces(self):
        """
        Convert the binary string to base64 url string with spaces and spaces and spaces.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_base64_url_with_spaces_and_spaces_and_spaces()
        'http://www.example.com/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111'

        """

    def convert_to_base64_url_with_spaces_and_spaces_and_spaces_and_spaces(self):
        """
        Convert the binary string to base64 url string with spaces and spaces and spaces and spaces.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_base64_url_with_spaces_and_spaces_and_spaces_and_spaces()
        'http://www.example.com/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111/0110100001100101011011000110110001101111'

        """

    def convert_to_base64_url_with_spaces_and_spaces_and_spaces_and_spaces_and_spaces(self):
        """
        Convert the binary string to base64 url string with