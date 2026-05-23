class NumericEntityUnescaper:
    """
    This is a class that provides functionality to replace numeric entities with their corresponding characters in a given string.
    """

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
        result = ""
        i = 0
        while i < len(string):
            if string[i] == "&":
                if i+2 < len(string) and string[i+1] == "#":
                    if string[i+2] == "x" or string[i+2] == "X":
                        hex_digits = string[i+3:i+9]
                        if len(hex_digits) == 0 or not all(NumericEntityUnescaper.is_hex_char(c) for c in hex_digits):
                            result += "&"
                        else:
                            result += chr(int(hex_digits, 16))
                        i += 8
                    else:
                        digits = string[i+2:i+8]
                        if len(digits) == 0 or not all(c.isdigit() for c in digits):
                            result += "&"
                        else:
                            result += chr(int(digits))
                        i += 7
                else:
                    j = string.find(";", i)
                    if j == -1:
                        result += "&"
                        i += 1
                    else:
                        entity = string[i+1:j]
                        if entity in HTML_ENTITIES:
                            result += HTML_ENTITIES[entity]
                        else:
                            result += "&"
                        i = j
            else:
                result += string[i]
                i += 1
        return result

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
        return char.isdigit() or (char >= 'a' and char <= 'f') or (char >= 'A' and char <= 'F')