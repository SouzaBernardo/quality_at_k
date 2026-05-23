
class BankAccount:  
    """
    This is a class as a bank account system, which supports deposit money, withdraw money, view balance, and transfer money.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance, default value is 0.
        """
        self.balance = balance



    def deposit(self, amount):
        
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance



    def withdraw(self, amount):


    def withdraw(self, amount):
        
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance


    def view_balance(self):
        

    def transfer(self, amount, other_account):
        
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        other_account.deposit(amount)
        return self.balance


    def transfer(self, amount, other_account):
        
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        other_account.deposit(amount)
        return self.balance


    def transfer(self, other_account, amount):
