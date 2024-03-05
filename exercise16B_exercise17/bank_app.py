from bank_accounts.current_account import CurrentAccount
from bank_accounts.savings_account import Savings
from bank_accounts.insufficient_funds_exception import OverdraftBreached

# OBJECT 1 - Instantiated an object of the Savings subclass
alex_account = Savings(93751, 'Alexander James Rodriguez', 600, 'savings', 5, 500, 500)

# No arguments passed will set the opening date to today
alex_account.set_opening_date()

# Prints main attributes of the alex_account object
print(alex_account)

# Insufficient Funds Exception raised
alex_account.withdraw(342)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# OBJECT 2 - Instantiated a 2nd object of the Savings subclass
chloe_account = Savings(45677, 'Chloe Matthews', 600, 'savings', 5, 500, 500)

# Arguments are passed to the chloe_account's setter method to set a specific opening date
chloe_account.set_opening_date(2, 2, 2022)

# Prints main attributes of the chloe_account object
print(chloe_account)

# Withdrawal Limit Exception raised
chloe_account.withdraw(511)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# OBJECT 3 - Instantiated a 3rd object of the Savings subclass
macy_account = Savings(45677, 'Macy Andrews', 800, 'savings', 5, 500, 500)

# Arguments are passed to the chloe_account's setter method to set a specific opening date
macy_account.set_opening_date(2, 2, 2022)

# Prints main attributes of the maxy_account object
print(macy_account)

# Withdrawal allowed
macy_account.withdraw(100)

# Updated balance
print(f'New Balance: £{macy_account.get_balance()}')

# print('//' * 20)
#
# # create an instance of CurrentAccount class with details specified and assign to jo_account variable
# jo_account = CurrentAccount('12345678', 'Joseph Nesbo', 1000,
#                             'current', 0)
#
# # use Jen's set_opening_date method to set an account opening date, otherwise returns None
# jo_account.set_opening_date(9, 10, 2016)
#
# # calls the special string method from account.py to print out the account information
# print(jo_account)
#
# print('*' * 25)
#
# # retrieve current balance of account and store in jo_balance variable
# jo_balance = jo_account.get_balance()
# print(f"Jo's current balance is £{jo_balance}")  # Jo's current balance is £1000
#
# # call the deposit method to add £50 to the account
# jo_account.deposit(50)
# # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
# jo_balance = jo_account.get_balance()
# print(f"Jo made a deposit, his new balance is £{jo_balance}")  # Jo made a deposit, his new balance is £1050
#
# # call the withdraw method to subtract £70 from the account
# jo_account.withdraw(70)
# # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
# jo_balance = jo_account.get_balance()
# print(f"Jo withdrew some money, his new balance is £{jo_balance}")  # Jo withdrew some money, his new balance is £980
#
# # # CODE written before implementing OverdraftBreached class
# # # a try block that contains code to be tested
# # # prints a message if balance goes below -100 as defined in the withdraw method
# # try:
# #     # call the withdraw method to subtract £1150 from the account
# #     jo_account.withdraw(1150)
# # # catch a ValueError if raised, trapping code and executing code to handle it
# # except ValueError as error:
# #     # prints the raised ValueError message defined in withdraw method
# #     print(error)  # Insufficient funds
# #
# # # try again with a smaller amount that doesn't raise an exception
# # try:
# #     jo_account.withdraw(900)
# # except ValueError as error:
# #     print(error)
# # # the try/except block does not catch an error
#
# try:
#     # call the withdraw method to subtract £1150 from the account
#     jo_account.withdraw(1150)
# # if the withdrawal exceeds overdraft limit then print custom error message defined in withdraw method
# except OverdraftBreached as error:
#     print(error)
# # Withdrawal denied. You will exceed your overdraft limit by £170
#
# # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
# jo_balance = jo_account.get_balance()
# print(f"Jo's current balance remains at £{jo_balance}")  # Jo's current balance remains at £980
#
# # try again with a smaller amount that doesn't raise an exception
# try:
#     jo_account.withdraw(900)
# except OverdraftBreached as error:
#     print(error)
#
# # retrieve updated balance and store in jo_balance variable, this will update the value stored inside jo_balance
# jo_balance = jo_account.get_balance()
# print(f"Jo withdrew less money this time, his new balance is £{jo_balance}")
# # Jo withdrew less money this time, his new balance is £80
#
# print('//' * 20)
