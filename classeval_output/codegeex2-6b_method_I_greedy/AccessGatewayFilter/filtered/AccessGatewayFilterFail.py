import logging
import datetime
class AccessGatewayFilter:  
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        pass



    def filter(self, request):
        
        return True


    def is_start_with(self, request_uri):
        
        return request_uri.startswith('/api/data')





    def set_current_user_info_and_log(self, user):
        
        
        request_uri = request.path
        if self.is_start_with(request_uri):
            logging.info('user: %s, request_uri: %s, time: %s' % (user['name'], request_uri, datetime.datetime.now()))