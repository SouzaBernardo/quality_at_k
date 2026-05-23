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
    def get_local_ip():
        """
        Get the local IP address.
        :return: string, the local IP address
        >>> IpUtil.get_local_ip()
        '127.0.0.1'
        >>> IpUtil.get_local_ip()
        '192.168.0.123'

        """


    @staticmethod
    def get_local_hostname():
        """
        Get the local hostname.
        :return: string, the local hostname
        >>> IpUtil.get_local_hostname()
        'www.baidu.com'
        >>> IpUtil.get_local_hostname()
        'www.baidu.com'

        """


    @staticmethod
    def get_local_ipv6():
        """
        Get the local IPv6 address.
        :return: string, the local IPv6 address
        >>> IpUtil.get_local_ipv6()
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        >>> IpUtil.get_local_ipv6()
        '2001:0db8:85a3::8a2e:0370:7334'

        """


    @staticmethod
    def get_local_ipv6_hostname():
        """
        Get the local IPv6 hostname.
        :return: string, the local IPv6 hostname
        >>> IpUtil.get_local_ipv6_hostname()
        'www.baidu.com'
        >>> IpUtil.get_local_ipv6_hostname()
        'www.baidu.com'

        """


    @staticmethod
    def get_local_ipv4_hostname():
        """
        Get the local IPv4 hostname.
        :return: string, the local IPv4 hostname
        >>> IpUtil.get_local_ipv4_hostname()
        'www.baidu.com'
        >>> IpUtil.get_local_ipv4_hostname()
        'www.baidu.com'

        """


    @staticmethod
    def get_local_ipv4():
        """
        Get the local IPv4 address.
        :return: string, the local IPv4 address
        >>> IpUtil.get_local_ipv4()
        '192.168.0.123'
        >>> IpUtil.get_local_ipv4()
        '192.168.0.123'

        """


    @staticmethod
    def get_local_ipv6_address():
        """
        Get the local IPv6 address.
        :return: string, the local IPv6 address
        >>> IpUtil.get_local_ipv6_address()
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        >>> IpUtil.get_local_ipv6_address()
        '2001:0db8:85a3::8a2e:0370:7334'

        """


    @staticmethod
    def get_local_ipv6_hostname():
        """
        Get the local IPv6 hostname.
        :return: string, the local IPv6 hostname
        >>> IpUtil.get_local_ipv6_hostname()
        'www.baidu.com'
        >>> IpUtil.get_local_ipv6_hostname()
        'www.baidu.com'

        """


    @staticmethod
    def get_local_ipv4_address():
        """
        Get the local IPv4 address.
        :return: string, the local IPv4 address
        >>> IpUtil.get_local_ipv4_address()
        '192.168.0.123'
        >>> IpUtil.get_local_ipv4_address()
        '192.168.0.123'

        """


    @staticmethod
    def get_local_ipv4_hostname():
        """
        Get the local IPv4 hostname.
        :return: string, the local IPv4 hostname
        >>> IpUtil.get_local_ipv4_hostname()
        'www.baidu.com'
        >>> IpUtil.get_local_ipv4_hostname()
        'www.baidu.com'

        """


    @staticmethod
    def get_local_ipv6_address_hostname():
        """
        Get the local IPv6 address and hostname.
        :return: string, the local IPv6 address and hostname
        >>> IpUtil.get_local_ipv6_address_hostname()
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334 www.baidu.com'
        >>> IpUtil.get_local_ipv6_address_hostname()
        '2001:0db8:85a3::8a2e:0370:7334 www.baidu.com'

        """


    @staticmethod
    def get_local_ipv6_address_hostname_port():
        """
        Get the local IPv6 address and hostname and port.
        :return: string, the local IPv6 address and hostname and port
        >>> IpUtil.get_local_ipv6_address_hostname_port()
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334:8080'
        >>> IpUtil.get_local_ipv6_address_hostname_port()
        '2001:0db8:85a3::8a2e:0370:7334:8080'

        """


    @staticmethod
    def get_local_ipv6_address_hostname_port_protocol():
        """
        Get the local IPv6 address and hostname and port and protocol.
        :return: string, the local IPv6 address and hostname and port and protocol
        >>> IpUtil.get_local_ipv6_address_hostname_port_protocol()
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334:8080:80'
        >>> IpUtil.get_local_ipv6_address_hostname_port_protocol()
        '2001:0db8:85a3::8a2e:0370:7334:8080:80'

        """


    @staticmethod
    def get_local_ipv6_address_hostname_port_protocol_port():
        """
        Get the local IPv6 address and hostname and port and protocol and port.
        :return: string, the local IPv6 address and hostname and port and protocol and port
        >>> IpUtil.get_local_ipv6_address_hostname_port_protocol_port()
        '2001:0db8:85a3:0000:0000:8a2e:0370:7334:8080:80'
        >>> IpUtil.get_local_ipv6_address_hostname_port_protocol_port()
        '2001:0db8:85a3::8a2e:037