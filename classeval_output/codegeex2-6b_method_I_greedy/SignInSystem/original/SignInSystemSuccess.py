
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
        
        if username not in self.users:
            self.users[username] = False
            return True
        else:
            return False


    def sign_in(self, username):


    def sign_in(self, username):
        

    def sign_out(self, username):


    def check_sign_in(self, username):


    def all_signed_in(self):


    def all_not_signed_in(self):
