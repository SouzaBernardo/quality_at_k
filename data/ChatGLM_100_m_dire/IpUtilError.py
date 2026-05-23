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
            socket.inet_aton(ip_address, socket.AF_INET)
            return True
        except socket.error as e:
            return False
        except:
            return False




    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :param ip_address:string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')
        '10.0.0.1'
        """
        if not ip_address.startswith('127.0.0.1'):
            return None
        try:
            socket.gethostbyaddr(ip_address[6:])
            return ip_address[:ip_address.index('127.0.0.1')]
        except socket.error as e:
            return None