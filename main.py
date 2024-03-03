class BankAccount:
    """A simple class representing a bank account.

    This class allows users to perform basic operations on their bank account,
    such as withdrawing and topping up funds.

    Attributes:
    - balance (int): The current balance of the bank account.

    Methods:
    - __init__(balance): Initializes a new bank account with the given balance.
    - withdraw(amount): Withdraws the specified amount from the account balance.
    - top_up(amount): Tops up the account balance with the specified amount.
    - __str__(): Returns a string representation of the account balance.

    Example usage:
    >>> example_account = BankAccount(100)
    >>> example_account.withdraw(50)
    >>> example_account.top_up(200)
    >>> print(example_account)
    You account balance is: 250
    """
    def __init__(self, balance):
        """Initializes a new bank account with the given balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Withdraws the specified amount from the account balance.

        Args:
        - amount (float): The amount to be withdrawn.

        Raises:
        - ValueError: If the amount is less than 1.
        """
        if amount > self.balance:
            print("Sorry, you don't have enough")
        elif amount < 1:
            raise ValueError("You can't withdraw less than 1")
        else:
            self.balance -= amount

    def top_up(self, amount):
        """Tops up the account balance with the specified amount.

        Args:
        - amount (float): The amount to be added to the account balance.

        Raises:
        - ValueError: If the amount is less than 1.
        """
        if amount < 1:
            print('Sorry, you can`t top up your account with an amount less than 1')
        else:
            self.balance += amount

    def __str__(self):
        """Returns a string representation of the account balance."""
        return f'You account balance is: {self.balance}'


account = BankAccount(100)
account.withdraw(50)
account.top_up(200)
print(account)
