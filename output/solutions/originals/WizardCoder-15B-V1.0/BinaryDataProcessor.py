Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class BinaryDataProcessor in the following code.
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

### Response:The class `BinaryDataProcessor` is already implemented and complete. The only thing that needs to be done is to add the implementation of the `clean_non_binary_chars` method. Here's the updated implementation:

```python
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
        """
        self.binary_string = ''.join(filter(str.isalnum, self.binary_string))

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        zeroes = self.binary_string.count('0')
        ones = self.binary_string.count('1')
        bit_length = len(self.binary_string)
        return {'Zeroes': zeroes / bit_length, 'Ones': ones / bit_length, 'Bit length': bit_length}

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        return self.binary_string.encode('ascii').decode('ascii')

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        return self.binary_string.encode('utf-8').decode('utf-8')
```

The `clean_non_binary_chars` method uses the `filter` function to remove all non-alphanumeric characters from the binary string. The `isalnum` method checks if a character is alphanumeric or not. The `join` method is used to join the filtered characters back into a string.

The `calculate_binary_info` method calculates the percentage of 0 and 1 in the binary string and the total length of the binary string. It returns a dictionary containing these values.

The `convert_to_ascii` and `convert_to_utf8` methods use the `encode` and `decode` methods to convert the binary string to ascii and utf-8 strings respectively. The `encode` method encodes the binary string into bytes, and the `decode` method decodes the bytes into a string.