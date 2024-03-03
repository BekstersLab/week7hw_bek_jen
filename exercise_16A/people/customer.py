# absolute import: specifying the full path to the module
# exercise_16A is a top level package, people is a subpackage, person is a module and Person is a class
from exercise_16A.people.person import Person


class Customer(Person):
    def __init__(self, firstname, middlename, lastname, email, account_number):
        # use super() to refer to the base or parent class
        # in this case we use super() to access the __init__ method from the Person class
        # calls the constructor function (__init__) from the parent class
        # Employee now uses parent class (Person) but adds its own stuff on
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.__account_number = account_number  # Unique to Customer
        self._purchase_total = 0

    def get_account_number(self):
        return self.__account_number

    def set_purchase_total(self, total):
        # Only try block will run if there is no exception, except block will not get executed
        try:
            self._purchase_total = round(total, 2)

        # If there is an exception, only except block will run, try block will be skipped
        except TypeError:

            print("Argument passed must be numbers for total cost in basket.")

    def get_purchase_total(self):

        return self._purchase_total

    def __add__(self, other):

        return self._purchase_total + other.get_purchase_total()

    def __str__(self):
        return (f'Firstname: {self.get_firstname()}\nMiddlename: {self.get_middlename()}\nLastname:'
                f' {self.get_lastname()}\nEmail: {self.get_email()}\nAccount Number: {self.__account_number}')


if __name__ == '__main__':

    customer1 = Customer('Mei', 'Ling', 'Chen', 'mei.chen@example.com', '01221234')

    print(customer1)

    customer1.set_purchase_total(1000.523)
    print('Purchase Total: £', customer1.get_purchase_total(), '\n')

    customer2 = Customer('Emily', 'Anne', 'Smith', 'emily.smith@example.com', '9876543210')
    customer2.set_purchase_total(10.523)
    print(customer2)
    print('Purchase Total: £', customer2.get_purchase_total(), '\n')

    print('Adding two object\'s total purchases', '£', customer1 + customer2)
