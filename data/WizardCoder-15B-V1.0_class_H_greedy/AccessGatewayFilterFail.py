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
        """
        if request['path'] == '/login' and request['method'] == 'POST':
            return True
        else:
            return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        prefixes = ['/api', '/admin']
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
        if 'Authorization' in request['headers']:
            auth_header = request['headers']['Authorization']
            if 'jwt' in auth_header:
                jwt_token = auth_header['jwt']
                # TODO: Validate the JWT token and get the user information
                return {'user': {'name': 'user1'}}
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # TODO: Set the current user information and log the access
        logging.info(f"User {user['name']} accessed the system at {datetime.datetime.now()}")