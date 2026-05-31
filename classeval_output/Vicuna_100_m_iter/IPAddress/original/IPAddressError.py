
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
        # code to implement the is_valid method
        pass

    def get_octets(self):
        if self.is_valid():
            return list(map(int, self.ip_address.split(".")))
        else:
            return []

    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
        if self.is_valid():
            return "".join(str(x) for x in self.get_octets())
        else:
            return ""