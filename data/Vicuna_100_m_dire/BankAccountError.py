class BankAccount: 
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
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
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
        >>> account1 = BankAccount()
        >>> account2 = BankAccount()
        >>> account1.deposit(1000)
        >>> account1.transfer(account2, 300)
        account1.balance = 700 account2.balance = 300
        """
        if self.balance < amount:
            raise ValueError("Insufficient balance to transfer.")
        if other_account.balance < amount:
            raise ValueError("Insufficient balance in the other account to transfer.")
        self.balance -= amount
        other_account.balance += amount