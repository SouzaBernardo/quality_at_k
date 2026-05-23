class NumberConverter:  
    """
    The class allows to convert  decimal to binary, octal and hexadecimal repectively and contrarily
    """



    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        """
        if decimal_num == 0:
            return '0'
        binary_num = ''
        while decimal_num > 0:
            binary_num = str(decimal_num % 2) + binary_num
            decimal_num //= 2
        return binary_num

    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        """
        decimal_num = 0
        power = len(binary_num) - 1
        for digit in binary_num:
            decimal_num += int(digit) * (2 ** power)
            power -= 1
        return decimal_num

    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        """
        if decimal_num == 0:
            return '0'
        octal_num = ''
        while decimal_num > 0:
            octal_num = str(decimal_num % 8) + octal_num
            decimal_num //= 8
        return octal_num





    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        """
        decimal_num = 0
        power = len(hex_num) - 1
        for digit in hex_num:
            decimal_num += int(digit, 16) * (16 ** power)
            power -= 1
        return decimal_num