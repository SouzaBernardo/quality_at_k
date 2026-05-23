class IpUtil:  
    """
    This is a class as tool for ip that can be used to obtain the local IP address, validate its validity, and also provides the functionality to retrieve the corresponding hostname.
    """


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
        ipv4_regex = re.compile(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

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
        ipv6_regex = re.compile(r'^(
            [0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|
            [0-9a-fA-F]{1,4}:){1,7}:|
            [0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|
            [0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|
            [0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|
            [0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|
            [0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|
            [0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|
            [0-9a-fA-F]{1,4}:){1,1}(:[0-9a-fA-F]{1,4}){1,6}|
            [0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,7}|:)|
            (([0-9a-fA-F]{1,4}:){1,8}[0-9a-fA-F]{1,4})
            )$')

    @staticmethod
        ipv6_regex_match(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address:string, the IP address to check
        :return:bool, True if the IP address is valid, False otherwise
        >>> IpUtil.ipv6_regex_match('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        True
        >>> IpUtil.ipv6_regex_match('2001:0db8:85a3:::8a2e:0370:7334')
        False

        """
        return IpUtil.ipv6_regex.match(ip_address) is not None

    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :param ip_address:string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')

        """
        ip_address = ip_address.strip()
        if IpUtil.is_valid_ipv4(ip_address):
            return socket.gethostbyaddr(ip_address)[0]
        elif IpUtil.is_valid_ipv6(ip_address):
            return socket.gethostbyaddr(ip_address)[0]
        else:
            return None

<|/ file |>
