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
        # Log the request details
        logging.info(f"Received request: {request}")
        # Check if the request method is POST and the path is /login
        if request['method'] == 'POST' and request['path'] == '/login':
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
            # Extract the JWT token from the request headers
            token = request['headers']['Authorization']['jwt']
            # Decode the JWT token to get the user information
            user_info = jwt.decode(token,'secret', algorithms=['HS256'])
            return user_info
        except Exception as e:
            logging.error(f"Error decoding JWT token: {e}")
            return None

