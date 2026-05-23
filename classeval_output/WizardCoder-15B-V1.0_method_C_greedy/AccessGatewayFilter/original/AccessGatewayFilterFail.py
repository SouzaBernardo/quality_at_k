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
        # Check if the request URI starts with '/api'
        if not self.is_start_with(request['path'], '/api'):
            logging.warning(f"Request to {request['path']} is not allowed")
            return False
        # Check if the request method is 'POST'
        if request['method']!= 'POST':
            logging.warning(f"Request with method {request['method']} is not allowed")
            return False
        # Get the JWT token from the request headers
        jwt_token = request.headers.get('Authorization')
        if not jwt_token:
            logging.warning("JWT token is missing in the request headers")
            return False
        # Validate the JWT token and get the user information
        user = self.get_jwt_user(jwt_token)
        if not user:
            logging.warning("Invalid JWT token")
            return False
        # Set the current user information and log the access
        self.set_current_user_info_and_log(user)
        # Allow the request
        return True

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        prefixes = ['/api/data', '/api/auth']
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
        try:
            token = request['headers']['Authorization']['jwt']
            decoded_token = jwt.decode(token,'secret', algorithms=['HS256'])
            return decoded_token['user']
        except Exception as e:
            logging.error(f"Error decoding JWT token: {e}")
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # TODO: Implement logging and access recording
        logging.info(f"User {user['name']} accessed at {datetime.datetime.now()}")