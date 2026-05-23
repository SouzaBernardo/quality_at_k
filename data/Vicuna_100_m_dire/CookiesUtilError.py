import json
class CookiesUtil: 
    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None



    def get_cookies(self, reponse):
        cookies = json.loads(reponse.headers['set-cookie'])
        self.cookies = cookies
        self._save_cookies()
        return cookies

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        try:
            with open(self.cookies_file, 'r') as f:
                cookies_data = json.load(f)
                self.cookies = cookies_data
        except FileNotFoundError:
            self.cookies = {}

    def _save_cookies(self):
        try:
            with open(self.cookies_file, 'w') as f:
                f.write(json.dumps(self.cookies))
            return True
        except FileNotFoundError:
            return False