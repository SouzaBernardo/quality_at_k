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
        """
        self.cookies = response.get('cookies', {})
        with open(self.cookies_file, 'w') as f:
            json.dump(self.cookies, f)
    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        with open(self.cookies_file, 'r') as f:
            self.cookies = json.load(f)
        return self.cookies
    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        try:
            with open(self.cookies_file, 'w') as f:
                json.dump(self.cookies, f)
            return True
        except Exception as e:
            print(f"An error occurred while saving cookies: {e}")
            return False