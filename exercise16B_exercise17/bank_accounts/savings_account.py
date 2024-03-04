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
        try:
            self._interest_rate = round(interest, 2)

        except TypeError:

            # Prints a string, reminding the user to pass numbers as an argument
            print("Error: Argument passed must be numbers for interest rate.")

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

        if amount <= self._withdraw_limit and self._min_balance <= abs(self._min_balance - amount):

            new_balance = self.get_balance() - amount

            self.set_balance(new_balance)

        elif amount > self._withdraw_limit:

            # raise WithdrawalLimitExceededError
            print('Withdrawal limit reached!')

        else:

            # raise InsufficientFundsError
            print('Not enough money!')

    def __str__(self):

        return (f'Account Number: {self.get_account_number()}\nAccount Holder Name: '
                f'{self.get_account_name()}\nAccount Type: {self.get_account_type()}\nCurrent Balance: '
                f'£{self.get_balance()}\n')


if __name__ == '__main__':

    chloe_account = Savings(45677, 'chloe', 300, 'savings', 5.12, 500, 500)
    # 5.12% AER/5.00% gross p.a. (£1 - £5,000)

    # chloe_account.set_interest_rate('5t')

    chloe_account.set_opening_date()

    print(chloe_account)

    chloe_account.withdraw(500)

    print(chloe_account)

