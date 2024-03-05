# absolute import of Account super class from account module
from exercise16B_exercise17.bank_accounts.account import Account
# absolute import of exception super classes from custom_exceptions module
from exercise16B_exercise17.bank_accounts.custom_exceptions import WithdrawalLimitExceededError, InsufficientFundsError
# imports datetime class from datetime module
from datetime import datetime


# class statement defines the Savings subclass that inherits Account, a super class
class Savings(Account):
    # def defines the CONSTRUCTOR method to initialise inherited attributes and new additional attributes
    def __init__(self, account_number, account_holder_name, balance, account_type, interest_rate, min_balance,
                 withdraw_limit):
        # calling super class' constructor method explicitly
        # to pass the necessary arguments that will initialize the Account super class' attributes and methods
        super().__init__(account_number, account_holder_name, balance, account_type)
        # Protected attributes must be accessed through methods
        self._interest_rate = interest_rate
        self._min_balance = round(min_balance, 2)
        self._withdraw_limit = round(withdraw_limit, 2)

    def get_interest_rate(self):  # defines the getter method to return the value of the interest rate

        return self._interest_rate  # returns the interest rate attribute

    def set_interest_rate(self, rate):  # defines the setter method to assign a new value to the interest rate

        self._interest_rate = rate  # assigns a new value to the interest rate attribute

    def get_min_balance(self):  # defines the getter method to return the value of the minimum balance required

        return self._min_balance  # returns the minimum balance attribute

    # InvalidMinimumBalanceError
    def set_min_balance(self, balance):  # defines the setter method to assign a new value as the minimum balance

        # rounds the new balance to 2 decimal places and assigns it to the minimum balance attribute
        self._min_balance = round(balance, 2)

    def get_withdraw_limit(self):  # defines the getter method to return the value of the withdrawal limit

        return self._withdraw_limit  # returns the withdrawal limit attribute

    def set_withdraw_limit(self, limit):  # defines the setter method to assign a new value as the withdrawal limit

        # rounds the new value to 2 decimal places and assigns it to the withdrawal limit attribute
        self._withdraw_limit = round(limit, 2)

    # defines a protected method to log exceptions, only to be called within this subclass
    def _log_exception(self, error_variable, file, exception_name):

        # datetime.now() returns datetime object with current date and time
        # strftime method formats datetime object into a string, assigned to now variable
        now = datetime.now().strftime("%d %b %Y %H:%M:%S")

        # write method writes a string to record the account number, name, exception, amount, date/time in a txt file
        file.write(f'{self.get_account_number()}-{self.get_account_name()}-{exception_name}: £{error_variable.amount} | '
                   f'Date/Time: {now}\n')

    # defines the withdrawal method to deduct an amount from the balance, takes one parameter
    def withdraw(self, amount):

        # try block will only run if no exceptions occur
        # An exception is an event that occurs, during execution, that disrupts the program from completing instructions
        try:
            # if block will execute if the withdrawal amount is less or equal to the withdrawal limit
            # AND the minimum balance required is less or equal to the new balance after withdrawal
            # abs function converts value to a positive number
            if amount <= self._withdraw_limit and self._min_balance <= (self.get_balance() - amount):

                # withdraw proceeds: amount is deducted from current balance, rounded to 2 decimal places
                # and assigned to new_balance variable
                new_balance = round(self.get_balance() - amount, 2)

                # the updated balance value is assigned to its attribute, using a setter method
                self.set_balance(new_balance)

            # if initial conditions are False and the withdrawal amount is more than the withdrawal limit, execute this.
            elif amount > self._withdraw_limit:

                # raising an exception means intentionally causing an error condition to occur
                # It signals that something unexpected happened and to handle it in a specific way
                # interrupts the normal flow of the program and transfers control to nearest exception handler
                raise WithdrawalLimitExceededError(amount)

            # if previous conditions are False, execute this code.
            else:
                raise InsufficientFundsError(amount)  # raises a custom exception to occur

        # if WithdrawalLLimitExceededError exception is raised, except statement catches it and assigns it to a variable
        except WithdrawalLimitExceededError as withdrawal_error:

            # prints exception statement of the withdrawal_error object
            print(withdrawal_error)

            # with statement will automatically close a file after opening it
            # open function opens exceptions_history.txt in append mode and assigns it to the file variable
            with open('exceptions_history.txt', 'a') as file:

                # 3 arguments are passed to the private log exception method to record the exception in a txt file
                self._log_exception(withdrawal_error, file, 'WithdrawalLimitExceededError')

        # if InsufficientFundsError exception is raised, except statement catches it and assigns it to a variable
        except InsufficientFundsError as funds_error:

            # prints the exception statement of the funds_error object
            print(funds_error)

            # with statement will automatically close a file after opening it
            # open function opens exceptions_history.txt in append mode and assigns it to the file variable
            with open('exceptions_history.txt', 'a') as file:

                # 3 arguments are passed to the private log exception method to record the exception in a txt file
                self._log_exception(funds_error, file, 'InsufficientFundsError')

        # finally statement is always executed, regardless if there's an exception or not
        # finally:
            # ensuring the file that was appended is closed
            # file.close()

    def __str__(self):  # Polymorphism, method overriding, changing the behaviour of special __str__ method

        # returns a string, stating the main attributes belonging to the current instance of the Savings subclass
        return (f'Account Number: {self.get_account_number()}\nAccount Holder Name: '
                f'{self.get_account_name()}\nAccount Type: {self.get_account_type()}\nCurrent Balance: '
                f'£{self.get_balance()}\n')


if __name__ == '__main__':

    chloe_account = Savings(45677, 'Chloe Matthews', 600, 'savings', 5, 500, 500)

    chloe_account.set_opening_date(2, 2, 2022)

    print(chloe_account)

    chloe_account.withdraw(333)

    print(chloe_account)
