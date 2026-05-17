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
        """
        Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        :param amount: int
        """

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").
        :param amount: int
        """

    def view_balance(self):
        """
        Return the account balance.
        """

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

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return "BankAccount(balance={0})".format(self.balance)


class BankAccountManager:
    """
    This class is a class that manages the bank account system.
    """

    def __init__(self):
        """
        Initializes a bank account manager object.
        """
        self.bank_accounts = {}

    def add_bank_account(self, account):
        """
        Adds a bank account to the bank account manager.
        :param account: BankAccount
        """
        self.bank_accounts[account.balance] = account

    def get_bank_account(self, balance):
        """
        Returns the bank account with the given balance.
        :param balance: int
        """
        return self.bank_accounts.get(balance)

    def get_bank_accounts(self):
        """
        Returns a list of all the bank accounts.
        """
        return list(self.bank_accounts.values())

    def get_bank_account_by_balance(self, balance):
        """
        Returns the bank account with the given balance.
        :param balance: int
        """
        return self.bank_accounts.get(balance)

    def get_bank_account_by_name(self, name):
        """
        Returns the bank account with the given name.
        :param name: str
        """
        return self.bank_accounts.get(name)

    def get_bank_accounts_by_name(self, name):
        """
        Returns a list of all the bank accounts with the given name.
        :param name: str
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_balance(self, balance):
        """
        Returns a list of all the bank accounts with the given balance.
        :param balance: int
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_balance_and_name(self, balance, name):
        """
        Returns a list of all the bank accounts with the given balance and name.
        :param balance: int
        :param name: str
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_balance_and_name_and_type(self, balance, name, type):
        """
        Returns a list of all the bank accounts with the given balance and name and type.
        :param balance: int
        :param name: str
        :param type: str
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_balance_and_name_and_type_and_type(self, balance, name, type, type_):
        """
        Returns a list of all the bank accounts with the given balance and name and type and type.
        :param balance: int
        :param name: str
        :param type: str
        :param type_: str
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_name_and_type(self, name, type):
        """
        Returns a list of all the bank accounts with the given name and type.
        :param name: str
        :param type: str
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_name_and_type_and_type(self, name, type, type_):
        """
        Returns a list of all the bank accounts with the given name and type and type.
        :param name: str
        :param type: str
        :param type_: str
        """
        return list(self.bank_accounts.values())

    def get_bank_accounts_by_name_and_type_and_type_and_type(self, name, type, type_, type_):
        """
        Returns a list of all the bank accounts with the given name and type and type.
        :param name: str
        :param type: str