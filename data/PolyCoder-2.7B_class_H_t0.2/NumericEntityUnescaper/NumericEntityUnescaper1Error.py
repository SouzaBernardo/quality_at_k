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


    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_hex_digit(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_digit('a')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_digit(char):
        """
        Determines whether a given character is a decimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a decimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_digit('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_digit_or_underscore(char):
        """
        Determines whether a given character is a decimal digit or underscore.
        :param char: str, the character to check.
        :return: bool, True if the character is a decimal digit or underscore, False otherwise.
        >>> NumericEntityUnescaper.is_digit_or_underscore('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_digit_or_underscore_or_hyphen(char):
        """
        Determines whether a given character is a decimal digit or underscore or hyphen.
        :param char: str, the character to check.
        :return: bool, True if the character is a decimal digit or underscore or hyphen, False otherwise.
        >>> NumericEntityUnescaper.is_digit_or_underscore_or_hyphen('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_digit_or_underscore_or_hyphen_or_underscore(char):
        """
        Determines whether a given character is a decimal digit or underscore or hyphen or underscore.
        :param char: str, the character to check.
        :return: bool, True if the character is a decimal digit or underscore or hyphen or underscore, False otherwise.
        >>> NumericEntityUnescaper.is_digit_or_underscore_or_hyphen_or_underscore('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_hyphen(char):
        """
        Determines whether a given character is a hyphen.
        :param char: str, the character to check.
        :return: bool, True if the character is a hyphen, False otherwise.
        >>> NumericEntityUnescaper.is_hyphen('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_hyphen_or_underscore(char):
        """
        Determines whether a given character is a hyphen or underscore.
        :param char: str, the character to check.
        :return: bool, True if the character is a hyphen or underscore, False otherwise.
        >>> NumericEntityUnescaper.is_hyphen_or_underscore('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_hyphen_or_underscore_or_hyphen(char):
        """
        Determines whether a given character is a hyphen or underscore or hyphen.
        :param char: str, the character to check.
        :return: bool, True if the character is a hyphen or underscore or hyphen, False otherwise.
        >>> NumericEntityUnescaper.is_hyphen_or_underscore_or_hyphen('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_underscore(char):
        """
        Determines whether a given character is a underscore.
        :param char: str, the character to check.
        :return: bool, True if the character is a underscore, False otherwise.
        >>> NumericEntityUnescaper.is_underscore('0')
        True

        """

        return (ord(char) >= 48 and ord(char) <= 57)

    @staticmethod
    def is_underscore_or_hyphen(char):
        """
        Determines whether a given character is a underscore or hyphen.
        :param char: str, the character to check.
        :return: bool, True if the character is a underscore or hyphen, False otherwise.
        >>> NumericEntityUnescaper.is_underscore_or_hyphen('