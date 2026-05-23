
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
        """
        octets = self.ip_address.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit():
                return False
            num = int(octet)
            if num < 0 or num > 255:
                return False
        return True
    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        """
        if self.is_valid():
            return self.ip_address.split('.')
        else:
            return []
    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        """
        if self.is_valid():
            octets = self.get_octets()
            binary_octets = [format(int(octet), '08b') for octet in octets]
            return '.'.join(binary_octets)
        else:
            return ''
    
