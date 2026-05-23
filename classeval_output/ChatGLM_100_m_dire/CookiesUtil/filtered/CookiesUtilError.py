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
        """
        Gets the cookies from the specified response, and save it to cookies_file.
        :param reponse: The response to get cookies from, dict.
        """
        if not reponse.get('cookies'):
            raise ValueError('cookies key not found in the response')
        self.cookies_file = cookies_file
        with open(self.cookies_file, 'w') as f:
            json.dump(self.cookies, f)

    def load_cookies(self):
        """
        Loads the cookies from the specified cookies file to the cookies data.
        :return: The cookies data, dict.
        """
        with open(self.cookies_file, 'r') as f:
             cookies = json.load(f)
        self.cookies = cookies

    def _save_cookies(self):
        """
        Saves the cookies to the specified cookies file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        if self.cookies is None:
            return False
        with open(self.cookies_file, 'w') as f:
            json.dump(self.cookies, f, indent=4)
        return True