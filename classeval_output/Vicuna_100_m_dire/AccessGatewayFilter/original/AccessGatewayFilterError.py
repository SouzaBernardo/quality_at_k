import logging
import datetime
class AccessGatewayFilter: 
    def __init__(self):
        pass



    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if request.get("path") == "/login" and request.get("method") == "POST":
            return True
        else:
            return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True

        >>> filter.is_start_with('/admin')
        True

        >>> filter.is_start_with('/')
        False
        """
        prefixes = ['/', '/api/', '/admin/']
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
        return False



