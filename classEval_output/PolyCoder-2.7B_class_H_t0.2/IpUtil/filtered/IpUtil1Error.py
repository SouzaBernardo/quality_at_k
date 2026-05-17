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
        >>> IpUtil.is_valid_ipv4('192.168.0.123')
        True
        >>> IpUtil.is_valid_ipv4('256.0.0.0')
        False

        """

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address:string, the IP address to check
        :return:bool, True if the IP address is valid, False otherwise
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        True
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
        False

        """


    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :param ip_address:string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')

        """


    @staticmethod
    def get_ipv4_address(ip_address):
        """
        Get the IPv4 address associated with the given IP address.
        :param ip_address:string, the IP address to get the IPv4 address for
        :return: string, the IPv4 address associated with the IP address
        >>> IpUtil.get_ipv4_address('192.168.0.123')
        '192.168.0.123'
        >>> IpUtil.get_ipv4_address('192.168.0.124')
        '192.168.0.124'
        >>> IpUtil.get_ipv4_address('192.168.0.125')
        '192.168.0.125'
        >>> IpUtil.get_ipv4_address('192.168.0.126')
        '192.168.0.126'
        >>> IpUtil.get_ipv4_address('192.168.0.127')
        '192.168.0.127'
        >>> IpUtil.get_ipv4_address('192.168.0.128')
        '192.168.0.128'
        >>> IpUtil.get_ipv4_address('192.168.0.129')
        '192.168.0.129'
        >>> IpUtil.get_ipv4_address('192.168.0.130')
        '192.168.0.130'
        >>> IpUtil.get_ipv4_address('192.168.0.131')
        '192.168.0.131'
        >>> IpUtil.get_ipv4_address('192.168.0.132')
        '192.168.0.132'
        >>> IpUtil.get_ipv4_address('192.168.0.133')
        '192.168.0.133'
        >>> IpUtil.get_ipv4_address('192.168.0.134')
        '192.168.0.134'
        >>> IpUtil.get_ipv4_address('192.168.0.135')
        '192.168.0.135'
        >>> IpUtil.get_ipv4_address('192.168.0.136')
        '192.168.0.136'
        >>> IpUtil.get_ipv4_address('192.168.0.137')
        '192.168.0.137'
        >>> IpUtil.get_ipv4_address('192.168.0.138')
        '192.168.0.138'
        >>> IpUtil.get_ipv4_address('192.168.0.139')
        '192.168.0.139'
        >>> IpUtil.get_ipv4_address('192.168.0.140')
        '192.168.0.140'
        >>> IpUtil.get_ipv4_address('192.168.0.141')
        '192.168.0.141'
        >>> IpUtil.get_ipv4_address('192.168.0.142')
        '192.168.0.142'
        >>> IpUtil.get_ipv4_address('192.168.0.143')
        '192.168.0.143'
        >>> IpUtil.get_ipv4_address('192.168.0.144')
        '192.168.0.144'
        >>> IpUtil.get_ipv4_address('192.168.0.145')
        '192.168.0.145'
        >>> IpUtil.get_ipv4_address('192.168.0.146')
        '192.168.0.146'
        >>> IpUtil.get_ipv4_address('192.168.0.147')
        '192.168.0.147'
        >>> IpUtil.get_ipv4_address('192.168.0.148')
        '192.168.0.148'
        >>> IpUtil.get_ipv4_address('192.168.0.149')
        '192.168.0.149'
        >>> IpUtil.get_ipv4_address('192.168.0.150')
        '192.168.0.150'
        >>> IpUtil.get_ipv4_address('192.168.0.151')
        '192.168.0.151'
        >>> IpUtil.get_ipv4_address('192.168.0.152')
        '192.168.0.152'
        >>> Ip