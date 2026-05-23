import logging
import datetime
class AccessGatewayFilter:  
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        pass



    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True
        """

        # Add your filtering logic here
        # For example, you can check if the request path is '/login' and the method is 'POST'
        if request['path'] == '/login' and request['method'] == 'POST':
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
        """
    
        prefixes = ['/api/', '/data/']  # Add your desired prefixes here
    
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
    
        return False
    

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        if 'headers' in request and 'Authorization' in request['headers']:
            auth_header = request['headers']['Authorization']
            if 'jwt' in auth_header:
                token = auth_header['jwt']
                try:
                    decoded_token = jwt.decode(token, algorithms=['HS256'])
                    return decoded_token.get('user')
                except jwt.exceptions.DecodeError:
                    return None
        return None
    

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        >>> filter = AccessGatewayFilter()
        >>> user = {'name': 'user1', 'address': '127.0.0.1'}
        >>> filter.set_current_user_info_and_log(user)
        """
        # Set the current user information
        self.current_user = user

        # Log the access
        logging.info(f"Access logged at {datetime.datetime.now()}: User {user['name']} accessed the system from {user['address']}")