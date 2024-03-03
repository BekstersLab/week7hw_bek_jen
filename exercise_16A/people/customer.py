# absolute import: specifying the full path to the module
# exercise_16A is a top level package, people is a subpackage, person is a module and Person is a class
from exercise_16A.people.person import Person


# class statement defines the Customer subclass that inherits Person, a super class
class Customer(Person):
    def __init__(self, firstname, middlename, lastname, email, account_number):
        # use super() to refer to the base or super class
        # in this case we use super() to access the __init__ method from the Person class
        # calls the constructor function (__init__) from the super class
        # Customer now has super class (Person) attributes and methods, but adds its own too
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.__account_number = account_number  # Unique to each object of the Customer class
        self._total_purchase = 0  # The total purchase on each customer's account, starting with a value of 0

    def get_account_number(self):  # def defines the get_account_number method

        return self.__account_number  # returns the account number attribute

    # def defines the set_total_purchase method to assign a value to self._total_purchase attribute
    def set_total_purchase(self, total):

        # try block will only run if there are no errors, except block will not get executed
        # An exception is an event that occurs, during execution, that disrupts the program from completing instructions
        try:

            # round function rounds the value of total to two decimal places
            # new value is assigned to self._purchase_total attribute
            self._total_purchase = round(total, 2)

        except TypeError:  # If there is an exception, try block is skipped and except block will run

            # Prints a string, reminding the user to pass numbers as an argument
            print("Argument passed must be numbers for total cost in basket.")

    def get_purchase_total(self):  # def defines the get_total_purchase method

        return self._total_purchase  # returns the total purchase attribute

    # POLYMORPHISM - Operator Overloading - changing the behaviour of a default operator for objects of this subclass
    def __add__(self, other):  # def redefines the behaviour of the special __add__ method

        # returns the sum of the total purchases of two instances of this subclass, Customer
        # other refers to another instance of this class
        return self._total_purchase + other.get_purchase_total()

    # POLYMORPHISM - Method Overriding - changing the behaviour of a special method for objects of the Customer subclass
    def __str__(self):  # def redefines the special __str__ method for the print() function

        # returns a string that outlines all the attributes belonging to the instance of this subclass, Customer
        return (f'Firstname: {self.get_firstname()}\nMiddlename: {self.get_middlename()}\nLastname:'
                f' {self.get_lastname()}\nEmail: {self.get_email()}\nAccount Number: {self.__account_number}')


# if statement checks special __name__ variable has the string value of __main__
# if true, means this script is being executed directly and not as a module
# if true, this block of code will be executed for testing
if __name__ == '__main__':

    # OBJECT 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # An object of the Customer subclass is instantiated with 5 arguments, object is assigned to customer1
    customer1 = Customer('Mei', 'Ling', 'Chen', 'mei.chen@example.com', '01221234')

    customer1.set_total_purchase(1000.523)  # sets the total amount spent in the customer1 object

    print(customer1)  # prints customer1 object, based on method overriding behaviour for special str method

    # prints the total amount spent by the customer1 object
    print(f'Purchase Total: £{customer1.get_purchase_total()}\n')

    # OBJECT 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Another object of the Customer subclass is instantiated with 5 arguments, object is assigned to customer2
    customer2 = Customer('Emily', 'Anne', 'Smith', 'emily.smith@example.com', '9876543210')

    customer2.set_total_purchase(10.523)  # sets the total amount spent in the customer2 object

    print(customer2)  # prints customer2 object, based on method overriding behaviour for special str method

    # prints the total amount spent by the customer2 object
    print(f'Purchase Total: £{customer2.get_purchase_total()}\n')

    # + operator overloading behaviour is applied on two objects, customer1 and customer
    # prints a string containing a sum of two objects' total purchases
    print(f'Sum of two object\'s total purchases: £{customer1 + customer2}')
