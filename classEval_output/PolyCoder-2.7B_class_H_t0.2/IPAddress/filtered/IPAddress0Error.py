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


    def get_address(self):
        """
        If the IP address is valid, return the IP address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_address()
        "10.10.10.10"
        """


    def get_network_address(self):
        """
        If the IP address is valid, return the network address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_network_address()
        "10.10.10.10"
        """


    def get_host_address(self):
        """
        If the IP address is valid, return the host address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_address()
        "10.10.10.10"
        """


    def get_port(self):
        """
        If the IP address is valid, return the port number as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_port()
        "10"
        """


    def get_domain(self):
        """
        If the IP address is valid, return the domain name as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_domain()
        "10.10.10.10"
        """


    def get_netmask(self):
        """
        If the IP address is valid, return the netmask as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_netmask()
        "255.255.255.0"
        """


    def get_broadcast(self):
        """
        If the IP address is valid, return the broadcast address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_broadcast()
        "255.255.255.255"
        """


    def get_netmask_int(self):
        """
        If the IP address is valid, return the netmask as an integer; otherwise, return 0
        :return: int
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_netmask_int()
        0
        """


    def get_broadcast_int(self):
        """
        If the IP address is valid, return the broadcast address as an integer; otherwise, return 0
        :return: int
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_broadcast_int()
        0
        """


    def get_network_mask(self):
        """
        If the IP address is valid, return the network mask as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_network_mask()
        "255.255.255.255"
        """


    def get_network_mask_int(self):
        """
        If the IP address is valid, return the network mask as an integer; otherwise, return 0
        :return: int
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_network_mask_int()
        0
        """


    def get_broadcast_int_int(self):
        """
        If the IP address is valid, return the broadcast address as an integer; otherwise, return 0
        :return: int
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_broadcast_int_int()
        0
        """


    def get_broadcast_int_str(