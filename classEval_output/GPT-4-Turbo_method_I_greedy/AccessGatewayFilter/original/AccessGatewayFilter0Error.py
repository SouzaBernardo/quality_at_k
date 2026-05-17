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
        # For simplicity, we only allow POST method to '/login' path
        if request['method'] == 'POST' and request['path'] == '/login':
            return True
        else:
            return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        # For simplicity, we only check if the URI starts with '/api'
        if request_uri.startswith('/api'):
            return True
        else:
            return False
    
    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        try:
            # Extract the Authorization header
            auth_header = request['headers']['Authorization']
    
            # Extract the user information and JWT token
            user_info = auth_header['user']
            jwt_token = auth_header['jwt']
    
            # For simplicity, we assume the JWT token is valid if it contains the user name and today's date
            if jwt_token == user_info['name'] + str(datetime.date.today()):
                return user_info
            else:
                return None
        except KeyError:
            # If the request does not contain the necessary headers, return None
            return None
    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # Set the current user information
        self.current_user = user
    
        # Log the access
        logging.info(f"User {user['name']} from {user['address']} accessed the system at {datetime.datetime.now()}")
