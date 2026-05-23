class IPAddress:
    """
    This is a class to process IP Address, including validating, getting the octets and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address


    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """


    def get_ip_address(self):
        """
        Return the IP address
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address()
        "10.10.10.10"
        """


    def get_ip_address_as_string(self):
        """
        Return the IP address as a string
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_string()
        "10.10.10.10"
        """


    def get_ip_address_as_binary_string(self):
        """
        Return the IP address as a binary string
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_string()
        "00001010.00001010.00001010.00001010"
        """


    def get_ip_address_as_decimal_string(self):
        """
        Return the IP address as a decimal string
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_decimal_string()
        "10101010101010"
        """


    def get_ip_address_as_binary_decimal_string(self):
        """
        Return the IP address as a binary decimal string
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string()
        "00001010.00001010.00001010.00001010"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros(self):
        """
        Return the IP address as a binary decimal string with leading zeros
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_leading_zeros()
        "00000000.00000000.00000000.00000000"
        """


    def get_ip_address_as_binary_decimal_string_with_trailing_zeros(self):
        """
        Return the IP address as a binary decimal string with trailing zeros
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_trailing_zeros()
        "00000000.00000000.00000000.00000001"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros(self):
        """
        Return the IP address as a binary decimal string with leading zeros and trailing zeros
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros()
        "00000000.00000000.00000000.00000001"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point(self):
        """
        Return the IP address as a binary decimal string with leading zeros and trailing zeros and decimal point
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point()
        "00000000.00000000.00000000.00000001"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros(self):
        """
        Return the IP address as a binary decimal string with leading zeros and trailing zeros and decimal point and leading zeros
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros()
        "00000000.00000000.00000000.00000001"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros_and_decimal_point(self):
        """
        Return the IP address as a binary decimal string with leading zeros and trailing zeros and decimal point and leading zeros and decimal point
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros_and_decimal_point()
        "00000000.00000000.00000000.00000001"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros_and_decimal_point_and_leading_zeros(self):
        """
        Return the IP address as a binary decimal string with leading zeros and trailing zeros and decimal point and leading zeros and decimal point and leading zeros
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros_and_decimal_point_and_leading_zeros()
        "00000000.00000000.00000000.00000001"
        """


    def get_ip_address_as_binary_decimal_string_with_leading_zeros_and_trailing_zeros_and_decimal_point_and_leading_zeros_and_decimal_point_and_leading_zeros_and_decimal_point_and_leading_zeros_and_decimal_point(self):
        """
        Return the IP address as a binary decimal string with leading zeros and trailing zeros and decimal point and leading zeros and decimal point and leading zeros and decimal point and leading zeros and decimal point
        :return: string
       