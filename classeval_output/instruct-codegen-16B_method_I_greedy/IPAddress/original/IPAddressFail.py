
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
        """
        ip_address_list = self.ip_address.split('.')
        if len(ip_address_list)!= 4:
            return False
        for item in ip_address_list:
            if not 0 <= int(item) <= 255:
                return False
        return True

    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        """
        if self.is_valid():
            ip_address_list = self.ip_address.split('.')
            return ip_address_list
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
            ip_address_list = self.ip_address.split('.')
            binary_list = []
            for item in ip_address_list:
                binary_list.append(bin(int(item)).replace('0b', ''))
            return ''.join(binary_list)
        else:
            return ''