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

    def convert_to_string(self):
        """
        Convert the binary string to string.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_string()
        '0110100001100101011011000110110001101111'

        """

    def convert_to_int(self):
        """
        Convert the binary string to int.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_int()
        0

        """

    def convert_to_float(self):
        """
        Convert the binary string to float.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_float()
        0.475

        """

    def convert_to_bool(self):
        """
        Convert the binary string to bool.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_bool()
        False

        """

    def convert_to_list(self):
        """
        Convert the binary string to list.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_list()
        ['0110100001100101011011000110110001101111']

        """

    def convert_to_dict(self):
        """
        Convert the binary string to dict.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_dict()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """

    def convert_to_list_of_dicts(self):
        """
        Convert the binary string to list of dicts.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_list_of_dicts()
        [
            {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40},
            {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40},
            {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40},
        ]

        """

    def convert_to_dict_of_lists(self):
        """
        Convert the binary string to dict of lists.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_dict_of_lists()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}

        """

    def convert_to_dict_of_dicts(self):
        """
        Convert the binary string to dict of dicts.
        >>> bdp = BinaryDataProcessor("0110100001100101011011000110110001101111")
        >>> bdp.convert_to_dict_of_dicts()
        {'Zeroes': 0.475, 'Ones': 0.525, 'Bit length': 40}