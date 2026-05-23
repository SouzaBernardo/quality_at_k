class NumericEntityUnescaper: 
    def __init__(self):
        pass



    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """
        result = ''
        i = 0
        while i < len(string):
            if string[i] == '&':
                if i + 1 < len(string) and string[i + 1] == '#':
                    i += 2
                    if i + 1 < len(string) and self.is_hex_char(string[i]):
                        hex_value = string[i]
                        i += 1
                        while i < len(string) and string[i].isdigit():
                            hex_value += string[i]
                            i += 1
                        try:
                            result += chr(int(hex_value, 16))
                        except ValueError:
                            result += '&' + hex_value + ';'
                    else:
                        result += '&'
                else:
                    result += '&'
            else:
                result += string[i]
            i += 1
        return result

    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
        return char.isdigit() or char.lower() in 'abcdef'