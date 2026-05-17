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
        If the IP address is valid, return the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address()
        "10.10.10.10"
        """


    def get_version(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version()
        "IPv4"
        """


    def get_version_string(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_string()
        "IPv4"
        """


    def get_version_number(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number()
        "4"
        """


    def get_version_number_string(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string()
        "4"
        """


    def get_version_number_string_with_dot(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string_with_dot()
        "4.4"
        """


    def get_version_number_string_with_dot_and_zero(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string_with_dot_and_zero()
        "4.4"
        """


    def get_version_number_string_with_dot_and_zero_and_zero(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string_with_dot_and_zero_and_zero()
        "4.4"
        """


    def get_version_number_string_with_dot_and_zero_and_one(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string_with_dot_and_zero_and_one()
        "4.4"
        """


    def get_version_number_string_with_dot_and_zero_and_two(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string_with_dot_and_zero_and_two()
        "4.4"
        """


    def get_version_number_string_with_dot_and_zero_and_three(self):
        """
        If the IP address is valid, return the version of the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_version_number_string_