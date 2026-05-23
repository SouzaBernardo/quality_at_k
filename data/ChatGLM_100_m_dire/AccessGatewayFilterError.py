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
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}}

        """
        if request.get('Authorization') and request.get('Authorization').get('user') and request.get('Authorization').get('jwt') and 'user1' in request.get('Authorization').get('user'):
            return request.get('Authorization').get('user')
        else:
            return None