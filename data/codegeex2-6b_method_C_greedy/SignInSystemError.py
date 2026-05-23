class SignInSystem: 
    def __init__(self):
        """
        Initialize the sign-in system.
        """
        self.users = {}



    def add_user(self, username):
        

        if username in self.users:
            return False
        else:
            self.users[username] = False
            return True


    def sign_in(self, username):


    def check_sign_in(self, username):


    def all_signed_in(self):


    def all_not_signed_in(self):