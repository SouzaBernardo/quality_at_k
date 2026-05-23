class IPAddress: 
    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address




    def is_valid(self):
        octets = self.get_octets()
        return len(octets) == 4 and all(0 <= int(n) <= 255 for n in octets)

    def get_octets(self):
        octets = self.ip_address.split(".")
        return octets

    def get_binary(self):
        octets = self.get_octets()
        binary_octets = [bin(int(numeric_octet))[2:].zfill(8) for numeric_octet in octets]
        return "".join(binary_octets)