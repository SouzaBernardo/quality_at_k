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


    def get_network_address(self):
        """
        If the IP address is valid, return the network address as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_network_address()
        "10.10.10.10"
        """


    def get_host_name(self):
        """
        If the IP address is valid, return the host name as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name()
        "10.10.10.10"
        """


    def get_host_name_and_port(self):
        """
        If the IP address is valid, return the host name and port as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name_and_port()
        "10.10.10.10:80"
        """


    def get_host_name_and_port_and_netmask(self):
        """
        If the IP address is valid, return the host name and port and netmask as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name_and_port_and_netmask()
        "10.10.10.10:80/255.255.255.255"
        """


    def get_host_name_and_port_and_netmask_and_ip(self):
        """
        If the IP address is valid, return the host name and port and netmask and ip as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name_and_port_and_netmask_and_ip()
        "10.10.10.10:80/255.255.255.255/255.255.255.255"
        """


    def get_host_name_and_port_and_netmask_and_ip_and_netmask(self):
        """
        If the IP address is valid, return the host name and port and netmask and ip and netmask as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name_and_port_and_netmask_and_ip_and_netmask()
        "10.10.10.10:80/255.255.255.255/255.255.255.255"
        """


    def get_host_name_and_port_and_netmask_and_ip_and_netmask_and_ip(self):
        """
        If the IP address is valid, return the host name and port and netmask and ip and netmask and ip as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name_and_port_and_netmask_and_ip_and_netmask_and_ip()
        "10.10.10.10:80/255.255.255.255/255.255.255.255"
        """


    def get_host_name_and_port_and_netmask_and_ip_and_netmask_and_ip_and_netmask(self):
        """
        If the IP address is valid, return the host name and port and netmask and ip and netmask and ip and ip as a string; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_host_name_and_port_and_netmask_and_ip_and_netmask_and_ip_and_netmask()
        "10.10.10.10:80/255.255.255.255/255.255.255.255"
        """


    def get_host_name_and_port_and_netmask_and_ip_and_netmask_and_ip_and_netmask_and_ip(self):