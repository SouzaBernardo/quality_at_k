
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
        octets = self.ip_address.split('.')
        for i in range(8):
            if len(octets) < 8 or octets[i] < 0 or octets[i] > 255:
                return False
            if octets[i] == 0:
                return False
            elif octets[i] == 1:
                if len(octets) < 7:
                    return False
                octets[i] = 0
            elif octets[i] == 2:
                if len(octets) < 6:
                    return False
                octets[i] = 0
            elif octets[i] == 3:
                if len(octets) < 5:
                    return False
                octets[i] = 0
            elif octets[i] == 4:
                if len(octets) < 4:
                    return False
                octets[i] = 0
            else:
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
        if self.is_valid():
            octets = self.ip_address.split('.')
            return [int(octet) for octet inoctets]
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
            octets = self.ip_address.split('.')
            return f"{octets[0]}.{octets[1]}.{octets[2]}.{octets[3]}"
        else:
            return ''