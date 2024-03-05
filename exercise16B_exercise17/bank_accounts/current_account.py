# import the Account superclass to inherit from it
from exercise16B_exercise17.bank_accounts.account import Account
# import the OverdraftBreached Exception class to handle overdrafts
from exercise16B_exercise17.bank_accounts.insufficient_funds_exception import OverdraftBreached


# create subclass which inherits from Account superclass
class CurrentAccount(Account):
    # constructor (__init__) with extra parameter (overdraft_allowance) to give subclass its own functionality
    # self refers to the current instance of the class e.g. jo_account variable.
    def __init__(self, account_number, account_holder_name, balance, account_type, overdraft_allowance):
        # use super() to access the constructor function (__init__)  from the superclass (Account)
        super().__init__(account_number, account_holder_name, balance, account_type)
        # specific to CurrentAccount only
        self._overdraft_allowance = overdraft_allowance

    def deposit(self, amount):
        # directly accesses the account's balance attribute from Account class (protected with single underscore)
        # increases the balance by the amount specified
        self._balance += amount

    #  # Withdrawal method written before implementing OverdraftBreached class
    # def withdraw(self, amount):
    #     # withdraw method checks if account will go below -100 (overdraft allowance)
    #     if self._balance - amount < -100:
    #         # if below -100 it raises a ValueError with a printed message
    #         raise ValueError("Insufficient funds available. Please try again!")
    #     else:
    #         # otherwise the withdrawn amount gets deducted from the balance
    #         self._balance -= amount

    # UPDATE withdraw method to incorporate separate exception file
    def withdraw(self, amount):
        # validates withdrawal amount, can't enter a negative value
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")

        # calculates the new balance after a withdrawal
        new_balance = self._balance - amount

        # checks if overdraft will be breached by withdrawal amount
        if new_balance >= self._overdraft_allowance:
            # if not breached then continue with withdrawal
            self._balance = new_balance
        else:
            # if overdraft breached then calculate amount
            # used abs() function - returns a positive version of a negative number
            # used this to change the -170 return in raised exception to update value in f-string ('£-170' now '£170')
            breach_amount = abs(new_balance - self._overdraft_allowance)
            # raise a custom exception and print the statement. breach_amount is determined in OverdraftBreached class
            raise OverdraftBreached(f"Withdrawal denied. You will exceed your overdraft limit by £{breach_amount}")


if __name__ == '__main__':

    print('//' * 20)

    # create an instance of CurrentAccount class with details specified and assign to jo_account variable
    jo_account = CurrentAccount('12345678', 'Joseph Nesbo', 1000,
                                'current', 0)

    # use Jen's set_opening_date method to set an account opening date, otherwise returns None
    jo_account.set_opening_date(9, 10, 2016)

    # calls the special string method from account.py to print out the account information
    print(jo_account)

    print('*' * 25)

    # retrieve current balance of account and store in jo_balance variable
    jo_balance = jo_account.get_balance()
    print(f"Jo's current balance is £{jo_balance}")  # Jo's current balance is £1000

    # call the deposit method to add £50 to the account
    jo_account.deposit(50)
    # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
    jo_balance = jo_account.get_balance()
    print(f"Jo made a deposit, his new balance is £{jo_balance}")  # Jo made a deposit, his new balance is £1050

    # call the withdraw method to subtract £70 from the account
    jo_account.withdraw(70)
    # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
    jo_balance = jo_account.get_balance()
    print(
        f"Jo withdrew some money, his new balance is £{jo_balance}")  # Jo withdrew some money, his new balance is £980

    # # CODE written before implementing OverdraftBreached class
    # # a try block that contains code to be tested
    # # prints a message if balance goes below -100 as defined in the withdraw method
    # try:
    #     # call the withdraw method to subtract £1150 from the account
    #     jo_account.withdraw(1150)
    # # catch a ValueError if raised, trapping code and executing code to handle it
    # except ValueError as error:
    #     # prints the raised ValueError message defined in withdraw method
    #     print(error)  # Insufficient funds
    #
    # # try again with a smaller amount that doesn't raise an exception
    # try:
    #     jo_account.withdraw(900)
    # except ValueError as error:
    #     print(error)
    # # the try/except block does not catch an error

    try:
        # call the withdraw method to subtract £1150 from the account
        jo_account.withdraw(1150)
    # if the withdrawal exceeds overdraft limit then print custom error message defined in withdraw method
    except OverdraftBreached as error:
        print(error)
    # Withdrawal denied. You will exceed your overdraft limit by £170

    # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
    jo_balance = jo_account.get_balance()
    print(f"Jo's current balance remains at £{jo_balance}")  # Jo's current balance remains at £980

    # try again with a smaller amount that doesn't raise an exception
    try:
        jo_account.withdraw(900)
    except OverdraftBreached as error:
        print(error)

    # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
    jo_balance = jo_account.get_balance()
    print(f"Jo withdrew less money this time, his new balance is £{jo_balance}")
    # Jo withdrew less money this time, his new balance is £80

    print('//' * 20)
