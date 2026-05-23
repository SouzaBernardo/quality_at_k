class SignInSystem:
    """
    This is a class as sigin in system, including adding users, signing in/out, checking sign-in status, and retrieving signed-in/not signed-in users.
    """

    def __init__(self):
        """
        Initialize the sign-in system.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
        >>> signInSystem.add_user("mike")
        True
        >>> signInSystem.add_user("mike")
        False
        """

    def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        >>> signInSystem.sign_in("mike")
        True
        >>> signInSystem.sign_in("mik")
        False
        """

    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """

    def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        >>> signInSystem.add_user("jack")
        True
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.all_signed_in()
        True
        """

    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.all_not_signed_in()
        ['a', 'b']
        """

    def get_signed_in_users(self):
        """
        Get a list of usernames that are signed in.
        :return: list[str], a list of usernames that are signed in.
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.get_signed_in_users()
        ['a', 'b']
        """


class SignInSystemTest(unittest.TestCase):
    """
    This is a class for testing the sign-in system.
    """

    def test_add_user(self):
        """
        Test add_user function.
        """
        signInSystem = SignInSystem()
        self.assertEqual(signInSystem.add_user("mike"), True)

    def test_sign_in(self):
        """
        Test sign_in function.
        """
        signInSystem = SignInSystem()
        self.assertEqual(signInSystem.sign_in("mike"), True)

    def test_check_sign_in(self):
        """
        Test check_sign_in function.
        """
        signInSystem = SignInSystem()
        self.assertEqual(signInSystem.check_sign_in("jack"), False)
        self.assertEqual(signInSystem.check_sign_in("mike"), True)

    def test_all_signed_in(self):
        """
        Test all_signed_in function.
        """
        signInSystem = SignInSystem()
        self.assertEqual(signInSystem.all_signed_in(), False)
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.all_signed_in(), True)

    def test_all_not_signed_in(self):
        """
        Test all_not_signed_in function.
        """
        signInSystem = SignInSystem()
        self.assertEqual(signInSystem.all_not_signed_in(), [])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.all_not_signed_in(), ['mike'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.all_not_signed_in(), ['mike', 'jack'])

    def test_get_signed_in_users(self):
        """
        Test get_signed_in_users function.
        """
        signInSystem = SignInSystem()
        self.assertEqual(signInSystem.get_signed_in_users(), [])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("mike")
        self.assertEqual(signInSystem.get_signed_in_users(), ['mike', 'jack'])
        signInSystem.add_user("jack")