import logging
import datetime
class AccessGatewayFilter: 
    def __init__(self):
        pass



    def filter(self, request):
        

        if request['method'] == 'GET':
            return True

        if request['method'] == 'POST':
            if request['path'] == '/login':
                return True

        return False


    def is_start_with(self, request_uri):
        
        return request_uri.startswith('/api/data')


    def get_jwt_user(self, request):
        

        if 'headers' not in request:
            return None

        if 'Authorization' not in request['headers']:
            return None

        if 'user' not in request['headers']['Authorization']:
            return None

        if 'jwt' not in request['headers']['Authorization']:
            return None

        if not request['headers']['Authorization']['jwt']:
            return None

        return request['headers']['Authorization']['user']


    def set_current_user_info_and_log(self, user):
        

        pass
