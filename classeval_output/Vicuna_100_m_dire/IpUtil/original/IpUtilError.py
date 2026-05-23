import socket
class IpUtil: 


    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
    
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        >>> IpUtil.is_valid_ipv4('192.168.0.123')
        True
        >>> IpUtil.is_valid_ipv4('256.0.0.0')
        False
    
        """
        try:
            socket.inet_aton(ip_address)
            return True
        except socket.error:
            return False

    def is_valid_ipv6(ip_address):
        socket = socket.socket(socket.AF_INET6)
        socket.settimeout(5)
        try:
            socket.connect(ip_address)
        except socket.error as e:
            return False
        socket.close()
        return True

    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
    
        :param ip_address: string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')
        '10.0.0.1'
        """
        try:
            socket.inet_aton(ip_address)
            hostname = socket.gethostbyname(ip_address)
            return hostname
        except socket.error:
            return ip_address