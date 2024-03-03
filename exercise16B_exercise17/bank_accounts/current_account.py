from account import Account


# create subclass of Account base class
class CurrentAccount(Account):
    # self refers to the current instance of the class eg. jo_account variable. Not added new parameters.
    def __init__(self, account_number, account_holder_name, balance, account_type):
        # use super() to access the __init__ method from the Account class
        # calls the constructor function (__init__) from the base class
        # CurrentAccount now uses base class (Account) but adds its own extra functionality
        super().__init__(account_number, account_holder_name, balance, account_type)  # Call the base class constructor

    def deposit(self, amount):
        # directly accesses the account's balance, increasing by the amount specified
        self._balance += amount

    def withdraw(self, amount):
        # withdraw method checks if account will go below -100 (overdraft allowance)
        if self._balance - amount < -100:
            # if below -100 it raises a ValueError with a printed message
            raise ValueError("Insufficient funds available. Please try again!")
        else:
            # otherwise the withdrawn amount gets deducted from the balance
            self._balance -= amount


# create an instance of CurrentAccount class with details specified and assign to jo_account variable
jo_account = CurrentAccount('12345678', 'Joseph Nesbo', 1000,
                            'current')

print(jo_account)

print('*' * 25)

# retrieve current balance of account and store in jo_balance variable
jo_balance = jo_account.get_balance()
print(f"Jo's current balance is £{jo_balance}")  # Jo's current balance is £1000

# call the deposit method to add £50 to the account
jo_account.deposit(50)
# retrieve updated balance and store in jo_balance variable, this will update the value stored inside the variable
jo_balance = jo_account.get_balance()
print(f"Jo made a deposit, his new balance is £{jo_balance}")  # Jo made a deposit, his new balance is £1050

# call the withdraw method to subtract £70 from the account
jo_account.withdraw(70)
# retrieve updated balance and store in jo_balance variable, this will update the value stored inside the variable
jo_balance = jo_account.get_balance()
print(f"Jo withdrew some money, his new balance is £{jo_balance}") # Jo withdrew some money, his new balance is £980

# a try/except block that prints a message if balance goes below -100 as defined in the withdraw method
try:
    # call the withdraw method to subtract £1150 from the account
    jo_account.withdraw(1150)
# catch a ValueError if raised
except ValueError as error:
    # prints the raised ValueError message defined in withdraw method
    print(error)  # Insufficient funds

# try again with a smaller amount that doesn't raise an exception
try:
    jo_account.withdraw(900)
except ValueError as error:
    print(error)
# the try/except block does not catch an error

# retrieve updated balance and store in jo_balance variable, this will update the value stored inside the variable
jo_balance = jo_account.get_balance()
print(f"Jo withdrew some money, his new balance is £{jo_balance}")  # Jo withdrew some money, his new balance is £80

