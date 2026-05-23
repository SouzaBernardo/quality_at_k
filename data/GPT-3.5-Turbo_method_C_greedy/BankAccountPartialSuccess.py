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
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance
    

    def view_balance(self):
        """
        Return the account balance.
        """
        return self.balance


    def transfer(self, other_account, amount):
        """
        Transfers a certain amount from the current account to another account.
        :param other_account: BankAccount
        :param amount: int
        """
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"account1.balance = {self.balance} account2.balance = {other_account.balance}")
        else:
            print("Insufficient balance.")