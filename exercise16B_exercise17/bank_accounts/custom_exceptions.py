class WithdrawalLimitExceededError(Exception):

    def __init__(self, amount):
        # super init method of the Exception super class is implicitly called
        # amount parameter is not expected and will not be used to initialize super class, Exception
        self.amount = amount

    def __str__(self):

        return f'Error: Requested amount of £{self.amount} exceeds the withdrawal limit.\n'


class InsufficientFundsError(Exception):
    def __init__(self, amount):
        self.amount = amount
        error_message = f'Error: Insufficient funds to withdraw £{amount}.\n'
        # passing the error_message parameter to super init method stores the error_message in the exception instance
        # Can be accessed directly through the instance or an assigned variable
        super().__init__(error_message)

