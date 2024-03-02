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
        self._account_number = account_number  # Unique to Customer

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Firstname: {self.first_name}\n'


if __name__ == '__main__':

    customer11 = Customer('Jane', 'A', 'Doe', 'jad12@gmail.com', '01221234')

    print(customer11)
