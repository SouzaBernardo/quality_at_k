
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
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
        decimal_num = 0
        power = 0
        for digit in binary_num[::-1]:
            decimal_num += int(digit) * pow(2, power)
            power += 1
        return decimal_num

    def decimal_to_octal(self, decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        """
        octal_num = ''
        while decimal_num > 0:
            octal_num = str(decimal_num % 8) + octal_num
            decimal_num //= 8
        return octal_num

    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        """
        decimal_num = 0
        power = 0
        for digit in octal_num[::-1]:
            decimal_num += int(digit) * pow(8, power)
            power += 1
        return decimal_num

    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        """
        hex_num = ''
        while decimal_num > 0:
            hex_num = str(decimal_num % 16) + hex_num
            decimal_num //= 16
        return hex_num

    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        """
        decimal_num = 0
        power = 0
        for digit in hex_num[::-1]:
            decimal_num += int(digit) * pow(16, power)
            power += 1
        return decimal_num