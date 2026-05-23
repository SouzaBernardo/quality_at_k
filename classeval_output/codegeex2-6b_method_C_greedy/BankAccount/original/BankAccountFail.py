
class BankAccount: 
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
        
        if amount < 0:
            raise ValueError("Invalid amount")
        elif amount > self.balance:
            raise ValueError("Insufficient balance.")
        else:
            self.balance -= amount
            return self.balance


    def view_balance(self):
        return self.balance


    def transfer(self, other_account, amount):
