
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
        if amount >= 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Invalid amount")

    def withdraw(self, amount):
        if amount >= 0:
            balance = self.balance - amount
            return balance
        else:
            raise ValueError("Invalid amount")

    def view_balance(self):
        """
        Returns the current balance of the account.
    
        :return: The current balance of the account.
        """
        return self.balance

    def transfer(self, other_account, amount):
            if other_account.balance > 0:
                other_account.balance -= amount
                self.balance += amount
                return amount
            else:
                raise ValueError("Invalid account")