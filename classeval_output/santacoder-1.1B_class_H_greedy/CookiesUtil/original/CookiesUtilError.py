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
        Sets the cookies data to the cookies_file.
        :param cookies: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.set_cookies({'key1': 'value1', 'key2': 'value2'})
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """

    def delete_cookies(self):
        """
        Deletes the cookies from the cookies_file.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.delete_cookies()
        >>> cookies_util.cookies
        None

        """

class CookiesUtilTest(unittest.TestCase):
    """
    This is a class as a unit test for CookiesUtil.
    """

    def setUp(self):
        """
        Sets up the test case.
        """
        self.cookies_util = CookiesUtil('cookies.json')

    def test_get_cookies(self):
        """
        Tests the get_cookies method.
        """
        self.cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        self.assertEqual(self.cookies_util.cookies, {'key1': 'value1', 'key2': 'value2'})

    def test_load_cookies(self):
        """
        Tests the load_cookies method.
        """
        self.cookies_util.load_cookies()
        self.assertEqual(self.cookies_util.cookies, {'key1': 'value1', 'key2': 'value2'})

    def test_save_cookies(self):
        """
        Tests the save_cookies method.
        """
        self.cookies_util.save_cookies()
        self.assertTrue(self._save_cookies())

    def test_set_cookies(self):
        """
        Tests the set_cookies method.
        """
        self.cookies_util.set_cookies({'key1': 'value1', 'key2': 'value2'})
        self.assertEqual(self.cookies_util.cookies, {'key1': 'value1', 'key2': 'value2'})

    def test_delete_cookies(self):
        """
        Tests the delete_cookies method.
        """
        self.cookies_util.delete_cookies()
        self.assertEqual(self.cookies_util.cookies, None)

if __name__ == '__main__':
    unittest.main()
