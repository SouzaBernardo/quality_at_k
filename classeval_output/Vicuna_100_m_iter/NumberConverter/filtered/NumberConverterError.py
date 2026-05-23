class NumberConverter:  
    """
    The class allows to convert  decimal to binary, octal and hexadecimal repectively and contrarily
    """



    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
        binary_string = ""
        while decimal_num > 0:
            binary_string = binary_string + str(decimal_num % 2)
            decimal_num = decimal_num // 2
        return binary_string

    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
        binary_string = binary_num.split('')
        decimal_num = 0
        for i in range(len(binary_string)):
            decimal_num = decimal_num * 2 ** (len(binary_string) - i - 1) + int(binary_string[i])
        return decimal_num

    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
        # code to convert decimal to octal
        # ...
        return octal_string

    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
        # code to convert octal to decimal
        # ...

    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """
        # code to convert decimal to hex
        # ...
        return hex_string

    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        >>> hex_to_decimal('a5b7')
        42423
        """
        # code to convert hex to decimal
        # ...
        return decimal_num