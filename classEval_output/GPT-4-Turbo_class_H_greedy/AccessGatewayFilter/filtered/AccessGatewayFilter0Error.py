import logging
import datetime
import jwt

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.current_user = None
        self.allowed_prefixes = ['/api', '/login']

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        if self.is_start_with(request.get('path')) and self.get_jwt_user(request):
            self.set_current_user_info_and_log(self.current_user)
            return True
        return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        return any(request_uri.startswith(prefix) for prefix in self.allowed_prefixes)

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        auth_header = request.get('headers', {}).get('Authorization')
        if auth_header:
            try:
                token = jwt.decode(auth_header, 'secret', algorithms=['HS256'])
                self.current_user = token.get('user')
                return self.current_user
            except jwt.InvalidTokenError:
                return None
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.current_user = user
        logging.info(f"User {user['name']} accessed at {datetime.datetime.now()}")