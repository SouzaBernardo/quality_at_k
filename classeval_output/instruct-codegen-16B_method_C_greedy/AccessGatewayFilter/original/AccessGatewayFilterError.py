import logging
import datetime
class AccessGatewayFilter: 
    def __init__(self):
        pass







    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        if 'Authorization' in request.headers and request.headers['Authorization'].startswith('Bearer '):
            token = request.headers['Authorization'].split()[1]
            try:
                jwt_user = JWTUser.objects.get(token=token)
                return {'user': jwt_user.user.username}
            except JWTUser.DoesNotExist:
                logger.warning('JWT token is invalid')
                return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # Get the current time
        now = datetime.datetime.now()
        # Create a log entry
        log_entry = 'User'+ user['name'] +'accessed the gateway at'+ str(now)
        # Log the entry
        logging.info(log_entry)