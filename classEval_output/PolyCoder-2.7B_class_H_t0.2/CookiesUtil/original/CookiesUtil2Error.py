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
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._save_cookies()
        True

        """

    def _set_cookies(self, cookies):
        """
        Sets the cookies to the cookies_file, and saves the cookies to the cookies_file.
        :param cookies: The cookies to set, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._set_cookies(cookies)
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """

    def _get_cookies(self):
        """
        Gets the cookies from the cookies_file, and returns a dict.
        :return: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._get_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """

    def save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util.save_cookies()
        True

        """

    def set_cookies(self, cookies):
        """
        Sets the cookies to the cookies_file, and saves the cookies to the cookies_file.
        :param cookies: The cookies to set, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util.set_cookies(cookies)
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """

    def delete_cookies(self):
        """
        Deletes the cookies from the cookies_file, and saves the cookies to the cookies_file.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util.delete_cookies()
        True

        """

    def get_cookie(self, key):
        """
        Gets the cookie value from the cookies_file, and saves the cookies to the cookies_file.
        :param key: The cookie key, str.
        :return: The cookie value, str.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util.get_cookie('key1')
        'value1'

        """

    def set_cookie(self, key, value):
        """
        Sets the cookie value in the cookies_file, and saves the cookies to the cookies_file.
        :param key: The cookie key, str.
        :param value: The cookie value, str.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util.set_cookie('key1', 'value1')
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """

    def delete_cookie(self, key):
        """
        Deletes the cookie in the cookies_file, and saves the cookies to the cookies_file.
        :param key: The cookie key, str.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util.delete_cookie('key1')
        True

    