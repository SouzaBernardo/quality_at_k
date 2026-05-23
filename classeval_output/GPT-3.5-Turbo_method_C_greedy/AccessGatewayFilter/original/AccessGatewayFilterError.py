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
        # Add your filtering logic here
        # For example, you can check if the request path starts with '/login' and the method is 'POST'
        if request['path'].startswith('/login') and request['method'] == 'POST':
            return True
        else:
            return False
    

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        prefixes = ['/api/data', '/api/users', '/api/products']  # Add your desired prefixes here
        return any(request_uri.startswith(prefix) for prefix in prefixes)
    

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        if 'headers' in request and 'Authorization' in request['headers']:
            token = request['headers']['Authorization']['jwt']
            try:
                decoded_token = jwt.decode(token, verify=False)
                return decoded_token['user']
            except jwt.DecodeError:
                return None
        else:
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
        logging.info(f"Access logged at {datetime.datetime.now()}: User {user['name']} accessed from {user['address']}")
