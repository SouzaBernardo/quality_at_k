class NumberConverter: 


    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
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
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
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
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
        octal_num = ""
        while decimal_num > 0:
            octal_num = str(decimal_num % 8) + octal_num
            decimal_num //= 8
        return octal_num if octal_num!= "" else "0"

    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
        decimal_num = 0
        for digit in octal_num:
            decimal_num = decimal_num * 8 + int(digit)
        return decimal_num

    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """
        hex_num = hex(decimal_num)[2:]
        return hex_num

    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
        decimal_num = 0
        hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
        for i in range(len(hex_num)):
            decimal_num += hex_dict[hex_num[i].lower()] * (16 ** (len(hex_num) - 1 - i))
        return decimal_num