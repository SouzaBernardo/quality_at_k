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
    def get_ip_address(hostname):
        """
        Get the IP address associated with the given hostname.
        :param hostname: string, the hostname to get the IP address for
        :return: string, the IP address associated with the hostname
        >>> IpUtil.get_ip_address('www.baidu.com')
        '110.242.68.3'
        >>> IpUtil.get_ip_address('10.0.0.1')
        '10.0.0.1'

        """

    @staticmethod
    def get_ip_address_by_hostname(hostname):
        """
        Get the IP address associated with the given hostname.
        :param hostname: string, the hostname to get the IP address for
        :return: string, the IP address associated with the hostname
        >>> IpUtil.get_ip_address_by_hostname('www.baidu.com')
        '110.242.68.3'
        >>> IpUtil.get_ip_address_by_hostname('10.0.0.1')
        '10.0.0.1'

        """


    @staticmethod
    def get_ip_address_by_ip(ip_address):
        """
        Get the IP address associated with the given IP address.
        :param ip_address: string, the IP address to get the IP address for
        :return: string, the IP address associated with the IP address
        >>> IpUtil.get_ip_address_by_ip('192.168.0.123')
        '192.168.0.123'
        >>> IpUtil.get_ip_address_by_ip('192.168.0.1')
        '192.168.0.1'

        """

    @staticmethod
    def get_ip_address_by_ip_and_hostname(ip_address, hostname):
        """
        Get the IP address associated with the given IP address and hostname.
        :param ip_address: string, the IP address to get the IP address for
        :param hostname: string, the hostname to get the IP address for
        :return: string, the IP address associated with the IP address and hostname
        >>> IpUtil.get_ip_address_by_ip_and_hostname('192.168.0.123', 'www.baidu.com')
        '192.168.0.123'
        >>> IpUtil.get_ip_address_by_ip_and_hostname('192.168.0.1', 'www.baidu.com')
        '192.168.0.1'

        """

    @staticmethod
    def get_ip_address_by_ip_and_hostname(ip_address, hostname):
        """
        Get the IP address associated with the given IP address and hostname.
        :param ip_address: string, the IP address to get the IP address for
        :param hostname: string, the hostname to get the IP address for
        :return: string, the IP address associated with the IP address and hostname
        >>> IpUtil.get_ip_address_by_ip_and_hostname('192.168.0.123', 'www.baidu.com')
        '192.168.0.123'
        >>> IpUtil.get_ip_address_by_ip_and_hostname('192.168.0.1', 'www.baidu.com')
        '192.168.0.1'

        """

    @staticmethod
    def get_ip_address_by_ip_and_hostname_and_port(ip_address, hostname, port):
        """
        Get the IP address associated with the given IP address and hostname and port.
        :param ip_address: string, the IP address to get the IP address for
        :param hostname: string, the hostname to get the IP address for
        :param port: int, the port to get the IP address for
        :return: string, the IP address associated with the IP address and hostname and port
        >>> IpUtil.get_ip_address_by_ip_and_hostname_and_port('192.168.0.123', 'www.baidu.com', 80)
        '192.168.0.123'
        >>> IpUtil.get_ip_address_by_ip_and_hostname_and_port('192.168.0.1', 'www.baidu.com', 80)
        '192.168.0.1'

        """

    @staticmethod
    def get_ip_address_by_ip_