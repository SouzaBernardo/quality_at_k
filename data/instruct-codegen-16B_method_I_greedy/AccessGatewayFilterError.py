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
        if request['path'] == '/login':
            self.logger.info('Received request to login')
            return True
        else:
            self.logger.info('Received request to access something else')
            return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        if request_uri.startswith('/api/data'):
            self.logger.info('Received request to access data')
            return True
        else:
            self.logger.info('Received request to access something else')
            return False

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        jwt_token = request['headers'].get('Authorization', None)
        if jwt_token is None:
            return None
        jwt_token_parts = jwt_token.split()
        if len(jwt_token_parts)!= 2 or jwt_token_parts[0]!= 'Bearer':
            return None
        jwt_token = jwt_token_parts[1]
        try:
            jwt_user = JWT.objects.get(token=jwt_token).user
            return User.objects.get(pk=jwt_user.pk)
        except JWT.DoesNotExist:
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        self.logger.info('User %s accessed the API', user['name'])
        JWT.objects.create(user=user, token=timezone.now())