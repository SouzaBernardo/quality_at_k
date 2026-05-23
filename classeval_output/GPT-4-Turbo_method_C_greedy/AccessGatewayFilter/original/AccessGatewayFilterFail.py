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
        # Check if the request path starts with '/login'
        if not self.is_start_with(request['path']):
            logging.error(f"Access denied for request: {request}")
            return False
    
        # Get the user from the JWT token in the request
        user = self.get_jwt_user(request)
    
        # If the user is not found, deny the request
        if user is None:
            logging.error(f"Access denied for request: {request}")
            return False
    
        # Set the current user info and log the access
        self.set_current_user_info_and_log(user)
    
        logging.info(f"Access granted for user: {user} at {datetime.datetime.now()}")
        return True
    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        prefixes = ['/api', '/auth', '/admin']  # Add or modify the prefixes as needed
        return any(request_uri.startswith(prefix) for prefix in prefixes)
    
    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            try:
                # Assuming the JWT token is in the 'jwt' field of the 'Authorization' header
                token = auth_header.get('jwt')
                # Decode the token. This will raise an exception if the token is invalid.
                # Replace 'your_secret_key' with the secret key used to encode the JWT token.
                payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
                return payload.get('user')
            except jwt.InvalidTokenError:
                logging.error('Invalid JWT token')
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.current_user = user
        logging.info(f"User {user['name']} from {user['address']} accessed at {datetime.datetime.now()}")
