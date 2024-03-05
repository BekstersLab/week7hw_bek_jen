# class defines the WithdrawalLimitExceededError subclass and inherits the Exception super class
class WithdrawalLimitExceededError(Exception):

    # defines the constructor method for this subclass with an additional attribute, amount
    def __init__(self, amount):
        # super init method of the Exception super class is implicitly called
        # amount parameter is not expected and will not be used to initialise super class, Exception
        self.amount = amount  # this attribute stores the attempted withdrawal amount

    # Polymorphism - method overriding - changed the behaviour of the special __str__ method
    def __str__(self):
        # returns a string, explaining why the Withdrawal Limit exception was raised
        return f'Error: Requested amount of £{self.amount} exceeds the withdrawal limit.\n'


# class defines InsufficientFundsError exception subclass and inherits the Exception super class
class InsufficientFundsError(Exception):

    # defines the constructor method for this subclass with an additional attribute, amount
    def __init__(self, amount):
        self.amount = amount  # this attribute stores the attempted withdrawal amount

        # this attribute stores a string to explain why the Insufficient Funds exception was raised
        error_message = f'Error: Insufficient funds to withdraw £{amount}.\n'

        # passing error_message to super constructor method stores the error_message in the instance of the super class
        # Can be accessed directly through the instance or an assigned variable
        super().__init__(error_message)
