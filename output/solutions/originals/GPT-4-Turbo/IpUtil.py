```python
import socket
import netifaces

class IpUtil:
    """
    This is a class as tool for ip that can be used to obtain the local IP address, validate its validity, and also provides the functionality to retrieve the corresponding hostname.
    """

    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        """
        try:
            socket.inet_pton(socket.AF_INET, ip_address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(ip_address)
            except socket.error:
                return False
            return ip_address.count('.') == 3
        except socket.error:  # not a valid address
            return False

        return True

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address:string, the IP address to check
        :return:bool, True if the IP address is valid, False otherwise
        """
        try:
            socket.inet_pton(socket.AF_INET6, ip_address)
        except socket.error:  # not a valid address
            return False
        return True

    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :param ip_address:string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return None
```