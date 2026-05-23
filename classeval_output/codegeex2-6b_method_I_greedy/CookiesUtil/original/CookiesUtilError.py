import json
class CookiesUtil:  
    """
    This is a class as utility for managing and manipulating Cookies, including methods for retrieving, saving, and setting Cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None



    def get_cookies(self, reponse):
        
        self.cookies = reponse['cookies']
        with open(self.cookies_file, 'w') as f:
            json.dump(self.cookies, f)


    def set_cookies(self, cookies):


    def load_cookies(self):


    def _save_cookies(self):
