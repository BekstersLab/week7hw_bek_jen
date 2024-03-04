from datetime import datetime


class Account:
    def __init__(self, account_number, account_holder_name, balance, account_type):
        self.__account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = round(balance, 2)
        self.__account_type = account_type
        self.__opening_date = None

    def get_account_number(self):

        return self.__account_number

    def set_account_name(self, name):

        self._account_holder_name = name

    def get_account_name(self):

        return self._account_holder_name

    def set_balance(self, balance):

        self._balance = balance

    def get_balance(self):

        return self._balance

    def set_account_type(self, account_type):

        self.__account_type = account_type

    def get_account_type(self):

        return self.__account_type

    def set_opening_date(self, day=None, month=None, year=None):

        if None in [day, month, year]:

            self.__opening_date = datetime.now().strftime('%d %b %Y')

        else:
            self.__opening_date = datetime(year, month, day).strftime('%d %b %Y')

    def get_opening_date(self):

        return self.__opening_date

    def __str__(self):
        return (f'Account Number: {self.__account_number}\nAccount Name: {self._account_holder_name}\nBalance: '
                f'£{self._balance}\nAccount Type: {self.__account_type}\nOpening Date: {self.__opening_date}')


if __name__ == '__main__':

    account_a = Account('ACCT123456789', 'John Doe', 1000.00, 'current')

    # if no arguments are passed, date is set to today
    account_a.set_opening_date()

    print(account_a, '\n')

    # 2nd Object ~~~~~~~~~~~~~~~~~~~~~

    account_b = Account('ACCT987654321', 'Jane Smith', 7500.50, 'savings')

    account_b.set_opening_date(5, 3, 2021)

    print(account_b)


