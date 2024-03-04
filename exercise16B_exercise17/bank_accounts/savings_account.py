from exercise16B_exercise17.bank_accounts.account import Account


class Savings(Account):
    def __init__(self, account_number, account_holder_name, balance, account_type, interest_rate, min_balance,
                 withdraw_limit):
        super().__init__(account_number, account_holder_name, balance, account_type)
        self._interest_rate = round(interest_rate, 2)
        self.__interest_earned = 0
        self._min_balance = round(min_balance, 2)
        self._withdraw_limit = round(withdraw_limit, 2)

    def get_interest_rate(self):

        return self._interest_rate

    # InvalidInterestRateError:
    def set_interest_rate(self, interest):

        self._interest_rate = round(interest, 2)

    def get_interest_earned(self):

        return self.__interest_earned

    def get_min_balance(self):

        return self._min_balance

    # InvalidMinimumBalanceError
    def set_min_balance(self, balance):

        self._min_balance = balance

    def get_withdraw_limit(self):

        return self._withdraw_limit

    def set_withdraw_limit(self, limit):

        self._withdraw_limit = limit

    # InsufficientFundsError & WithdrawalLimitExceededError
    def withdraw(self, amount):

        new = self.get_balance() - amount

        self.set_balance(new)


if __name__ == '__main__':

    chloe_account = Savings(45677, 'chloe', 300, 'savings', 5.12, 500, 500)
    # 5.12% AER/5.00% gross p.a. (£1 - £5,000)

