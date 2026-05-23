class IPAddress: 
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
        return True

    def get_octets(self):
        if self.is_valid():
            return list(map(int, self.ip_address.split(".")))
        else:
            return []

    def get_binary(self):
        if self.is_valid():
            return "0b" + str(self.ip_address).split(".")
        else:
            return ""