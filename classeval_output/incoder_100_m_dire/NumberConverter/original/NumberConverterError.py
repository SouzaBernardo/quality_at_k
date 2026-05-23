
class NumberConverter: 


    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """


    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """



    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """


    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """


    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """


    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
        hex_num = hex_num.upper()
        hex_digits = hex_num[2:]
        hex_digits = hex_digits.zfill(4)
        hex_digits = hex_digits.upper()
        hex_digits = hex_digits.replace('0', '')
        hex_digits = hex_digits.replace('1', '')
        hex_digits = hex_digits.replace('2', '')
        hex_digits = hex_digits.replace('3', '')
        hex_digits = hex_digits.replace('4', '')
        hex_digits = hex_digits.replace('5', '')
        hex_digits = hex_digits.replace('6', '')
        hex_digits = hex_digits.replace('7', '')
        hex_digits = hex_digits.replace('8', '')
        hex_digits = hex_digits.replace('9', '')
        hex_digits = hex_digits.replace('A', '')
        hex_digits = hex_digits.replace('B', '')
        hex_digits = hex_digits.replace('C', '')
        hex_digits = hex_digits.replace('D', '')
        hex_digits = hex_digits.replace('E', '')
        hex_digits = hex_digits.replace('F', '')
        hex_digits = hex_digits.replace('G', '')
        hex_digits = hex_digits.replace('H', '')
        hex_digits = hex_digits.replace('I', '')
        hex_digits = hex_digits.replace('J', '')
        hex_digits = hex_digits.replace('K', '')
        hex_digits = hex_digits.replace('L', '')
        hex_digits = hex_digits.replace('M', '')
        hex_digits = hex_digits.replace('N', '')
        hex_digits = hex_digits.replace('O', '')
        hex_digits = hex_digits.replace('P', '')
        hex_digits = hex_digits.replace('Q', '')
        hex_digits = hex_digits.replace('R', '')
        hex_digits = hex_digits.replace('S', '')
        hex_digits = hex_digits.replace('T', '')
        hex_digits = hex_digits.replace('U', '')
        hex_digits = hex_digits.replace('V', '')
        hex_digits = hex_digits.replace('W', '')
        hex_digits = hex_digits.replace('X', '')
        hex_digits = hex_digits.replace('Y', '')
        hex_digits = hex_digits.replace('Z', '')
        hex_digits = hex_digits.replace('a', '')
        hex_digits = hex_digits.replace('b', '')
        hex_digits = hex_digits.replace('c', '')
        hex_digits = hex_digits.replace('d', '')
        hex_digits = hex_digits.replace('e', '')
        hex_digits = hex_digits.replace('f', '')
        hex_digits = hex_digits.replace('g', '')
        hex_digits = hex_digits.replace('h', '')
        hex_digits = hex_digits.replace('i', '')
        hex_digits = hex_digits.replace('j', '')
        hex_digits = hex_digits.replace('k', '')
        hex_digits = hex_digits.replace('l', '')
        hex_digits = hex_digits.replace('m', '')
        hex_digits = hex_digits.replace('n', '')
        hex_digits = hex_digits.replace('o', '')
        hex_digits = hex_digits.replace('p', '')
        hex_digits = hex_digits.replace('q', '')
        hex_digits = hex_digits.replace('r', '')
        hex_digits = hex_digits.replace('s', '')
        hex_digits = hex_digits.replace('t', '')
        hex_digits = hex_digits.replace('u', '')
        hex_digits = hex_digits.replace('v', '')
        hex_digits = hex_digits.replace('w', '')
        hex_digits = hex_digits.replace('x', '')
        hex_digits = hex_digits.replace('y', '')
        hex_digits = hex_digits.replace('z', '')
        hex_digits = hex_digits.replace(' ', '')
        hex_digits = hex_digits.replace(',', '')
        hex_digits = hex_digits.replace(':', '')
        hex_digits = hex_digits.replace(';', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('?', '')
        hex_digits = hex_digits.replace('+', '')
        hex_digits = hex_digits.replace('/', '')
        hex_digits = hex_digits.replace('=', '')
        hex_digits = hex_digits.replace('_', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        hex_digits = hex_digits.replace(')', '')
        hex_digits = hex_digits.replace('!', '')
        hex_digits = hex_digits.replace('@', '')
        hex_digits = hex_digits.replace('#', '')
        hex_digits = hex_digits.replace('$', '')
        hex_digits = hex_digits.replace('%', '')
        hex_digits = hex_digits.replace('^', '')
        hex_digits = hex_digits.replace('&', '')
        hex_digits = hex_digits.replace('*', '')
        hex_digits = hex_digits.replace('(', '')
        return int(hex_digits, 
