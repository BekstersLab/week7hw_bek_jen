class WithdrawalLimitExceededError(Exception):

    def __init__(self, amount, error_message = f'Error: Requested amount exceeds withdrawal limit.'):
        self.amount = amount
        # passing the error_message parameter to super init method stores the error_message in the exception instance
        # Can be accessed directly through the instance or an assigned variable
        super().__init__(error_message)


class InsufficientFundsError(Exception):
    def __init__(self, amount, error_message='Error: Insufficient funds to withdraw.'):
        self.amount = amount
        super().__init__(error_message)

