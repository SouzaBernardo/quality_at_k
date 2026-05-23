
class IPAddress: 
    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address




    def is_valid(self):


    def get_octets(self):
        

        if self.is_valid():
            return self.ip_address.split(".")
        else:
            return []


    def get_binary(self):
        

        if self.is_valid():
            octets = self.get_octets()
            binary_octets = []
            for octet in octets:
                binary_octet = bin(int(octet))[2:].zfill(8)
                binary_octets.append(binary_octet)
            return ".".join(binary_octets)
        else:
            return ""
