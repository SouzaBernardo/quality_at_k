
class NumberConverter: 


    def decimal_to_binary(decimal_num):
        binary_num = 0
        while decimal_num > 0:
            binary_num = decimal_num % 2 ** 3 + binary_num // 2 ** 0
            decimal_num = decimal_num // 2 ** 1
        return binary_num

    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
        binary_num = binary_num.strip('0b')
        binary_list = binary_num.split ' '
        decimal_num = 0
        for bit in binary_list:
            if bit.startswith('0'):
                decimal_num = decimal_num * 2 + int(bit[1:])
            else:
                decimal_num = decimal_num * 2 + int(bit)
        return decimal_num

    def decimal_to_octal(decimal_num):
        return str(decimal_num)

    def octal_to_decimal(octal_num):
        # Convert the octal number to a binary number
        binary_num = bin(int(octal_num, 8))
    
        # Convert the binary number to a decimal number
        decimal_num = sum(int(digit) for digit in binary_num)
    
        return decimal_num

    def decimal_to_hex(decimal_num):
        return hex(decimal_num)

    def hex_to_decimal(hex_num):
        # Convert the hex string to an integer
        hex_num = int(hex_num, 16)
        # Convert the integer to a decimal number
        return hex_num