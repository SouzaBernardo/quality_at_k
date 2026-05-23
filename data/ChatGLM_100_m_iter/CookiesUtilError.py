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
        """
        Gets the cookies from the specified response,and save it to cookies_file.
        :param reponse: The response to get cookies from, dict.
        """
        if not reponse.get('cookies'):
            raise ValueError('cookies key not found in response')
        with open(self.cookies_file, 'w') as f:
            json.dump(reponse['cookies'], f)

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """
        with open(self.cookies_file, 'r') as f:
            self.cookies = json.load(f)

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        with open(self.cookies_file, 'w') as f:
            if self.cookies is None:
                self.cookies = {}
            json.dump(self.cookies, f)
        return True