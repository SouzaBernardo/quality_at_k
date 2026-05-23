
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
        ip_octets = self.ip_address.split(".")
        if len(ip_octets) != 4:
            return False
        for octet in ip_octets:
            try:
                octet = int(octet)
                if octet < 0 or octet > 255:
                    return False
            except ValueError:
                return False
        return True


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
        ip_octets = self.ip_address.split(".")
        return ip_octets


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
        ip_octets = str(self.ip_address)
        ip_octets = ip_octets.split(".")
        ip_octets = [int(i) for i in ip_octets]
        ip_octets.reverse()
        ip_octets = ".".join(map(str, ip_octets))
        return ip_octets
