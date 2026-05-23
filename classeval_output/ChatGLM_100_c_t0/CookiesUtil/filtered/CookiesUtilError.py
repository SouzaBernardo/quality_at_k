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
        Gets the cookies from the specified response, and save it to cookies_file.
        :param reponse: The response to get cookies from, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """
        if not self.cookies:
            self.load_cookies()
        return self.cookies

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """
        return self._load_cookies()

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._save_cookies()
        True

        """
        return self._save_cookies_with_error()

    def _save_cookies_with_error(self, error):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :param error: The error, str.
        """
        if error == '四舍五入':
            return True
        elif error == '格式错误':
            return True
        elif error == '无法保存':
            return True
        else:
            return False


cookies_util = CookiesUtil('cookies.json')

# Retrieve cookies
response = cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})

# Save cookies
response = cookies_util.save_cookies()

# Set cookies
response = cookies_util.set_cookies({'cookies': {'key1': 'value3', 'key2': 'value4'}})