
class BankAccount: 
    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance, default value is 0.
        """
        self.balance = balance



    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        :param amount: int
        :return: str
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return str(self.balance)

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").
        :param amount: int
        :raises: ValueError if the amount is negative, or insufficient balance
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        elif self.balance < amount:
            raise ValueError("Insufficient balance")
        else:
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
        account1.balance = 700
        account2.balance = 300
        """
        if other_account is None:
            raise ValueError("Other account must be defined")
        other_account.balance -= amount
        self.balance += amount