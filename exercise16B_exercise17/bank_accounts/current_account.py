from account import Account


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, account_type):
        # use super() to refer to the base class
        # in this case we use super() to access the __init__ method from the Account class
        # calls the constructor function (__init__) from the base class
        # CurrentAccount now uses base class (Account) but adds its own extra functionality
        super().__init__(account_number, account_holder_name, balance, account_type)  # Call the base class constructor







# one function
# get adders
# withdraw? Throw exception? Error handling...
