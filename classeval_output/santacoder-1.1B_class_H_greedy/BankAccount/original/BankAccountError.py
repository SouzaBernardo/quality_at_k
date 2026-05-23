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


class BankAccountTest(unittest.TestCase):
    """
    This is a class as a bank account system, which supports deposit money, withdraw money, view balance, and transfer money.
    """

    def test_deposit(self):
        """
        Test deposit method.
        """
        account = BankAccount()
        self.assertEqual(account.deposit(100), 100)

    def test_withdraw(self):
        """
        Test withdraw method.
        """
        account = BankAccount()
        self.assertEqual(account.withdraw(100), 100)

    def test_view_balance(self):
        """
        Test view balance method.
        """
        account = BankAccount()
        self.assertEqual(account.view_balance(), 0)

    def test_transfer(self):
        """
        Test transfer method.
        """
        account1 = BankAccount()
        account2 = BankAccount()
        account1.deposit(100)
        account2.deposit(100)
        account1.transfer(account2, 100)
        self.assertEqual(account1.balance, 900)
        self.assertEqual(account2.balance, 900)


if __name__ == '__main__':
    unittest.main()
