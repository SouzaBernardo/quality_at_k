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


    def get_ip_address_as_string(self):
        """
        If the IP address is valid, return the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_string()
        "10.10.10.10"
        """


    def get_ip_address_as_int(self):
        """
        If the IP address is valid, return the IP address as an integer; otherwise, return 0
        :return: int
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_int()
        0
        """


    def get_ip_address_as_long(self):
        """
        If the IP address is valid, return the IP address as a long; otherwise, return 0
        :return: long
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_long()
        0
        """


    def get_ip_address_as_float(self):
        """
        If the IP address is valid, return the IP address as a float; otherwise, return 0
        :return: float
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_float()
        0
        """


    def get_ip_address_as_double(self):
        """
        If the IP address is valid, return the IP address as a double; otherwise, return 0
        :return: double
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_double()
        0
        """


    def get_ip_address_as_bytes(self):
        """
        If the IP address is valid, return the IP address as a byte array; otherwise, return ''
        :return: byte array
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_bytes()
        b'00001010.00001010.00001010.00001010'
        """


    def get_ip_address_as_string_list(self):
        """
        If the IP address is valid, return the IP address as a string list; otherwise, return an empty list
        :return: string list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_string_list()
        []
        """


    def get_ip_address_as_int_list(self):
        """
        If the IP address is valid, return the IP address as an integer list; otherwise, return an empty list
        :return: int list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_int_list()
        []
        """


    def get_ip_address_as_long_list(self):
        """
        If the IP address is valid, return the IP address as a long list; otherwise, return an empty list
        :return: long list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_long_list()
        []
        """


    def get_ip_address_as_float_list(self):
        """
        If the IP address is valid, return the IP address as a float list; otherwise, return an empty list
        :return: float list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_ip_address_as_float_list()
        []
        """


    def get_ip_address_as_double_list(self):
        """
        If