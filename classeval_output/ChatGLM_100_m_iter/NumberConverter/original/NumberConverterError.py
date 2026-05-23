
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
        if decimal_num < 0 or decimal_num > 127:
            raise ValueError("Invalid decimal number")
        
        binary = ""
        for i in range(1, 25):
            binary += str(decimal_num % 2**i)
        
        return binary

    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
        return binary_to_decimal(binary_num).int()




    def octal_to_decimal( octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter. octal_to_decimal('122667')
        42423
        """
        if octal_num < 0 or octal_num > 127:
            raise ValueError("Invalid octal number")
        
        decimal = decimal_to_binary( octal_num)
        binary = ""
        for i in range(1, 25):
            binary += str(decimal % 2**i)
        
        return binary_to_decimal(binary).int()

    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """
        if decimal_num < 0 or decimal_num > 127:
            raise ValueError("Invalid decimal number")
        
        binary = ""
        for i in range(1, 25):
            binary += str(decimal_num % 2**i)
        
        return binary.lower()

    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        """
        if hex_num < 0 or hex_num > 127:
            raise ValueError("Invalid hex number")
        
        binary = ""
        for i in range(1, 25):
            binary += str(hex_num % 2**i)
        
        return binary.lower()