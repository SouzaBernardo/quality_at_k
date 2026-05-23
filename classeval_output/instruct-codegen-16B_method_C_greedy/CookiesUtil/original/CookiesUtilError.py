import json
class CookiesUtil: 
    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None



    def get_cookies(self, response):
        """
        Gets the cookies from the specified response,and save it to cookies_file.
        :param response: The response to get cookies from, dict.
        :return: The retrieved cookies, dict.
        """
        if not self.cookies:
            self.load_cookies()
        if 'cookies' in response:
            cookies = response['cookies']
        else:
            cookies = {}
        self.cookies.update(cookies)
        self._save_cookies()
        return self.cookies



