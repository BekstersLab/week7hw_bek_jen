# inherit from Python's built in Exception class, therefore access the functionality of a standard Python exception
# includes ability to be raised with a raise statement and caught with a try block
class OverdraftBreached(Exception):

    # constructor (__init__) initialises the exception with the overdraft breach amount
    # allows exception to hold information on how much withdrawal attempt exceeds overdraft limit
    # amount is used
    def __init__(self, breach_amount):
        # stores the breach amount for reference in error messages
        self.breach_amount = breach_amount


# class contains minimal attributes needed to handle errors
# additional attributes could be added later
