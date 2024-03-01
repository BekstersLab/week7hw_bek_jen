from people.person import Person


class Customer(Person):
    def __init__(self, firstname, middlename, lastname, email, account_number):
        # use super() to refer to the base or parent class
        # in this case we use super() to access the __init__ method from the Person class
        # calls the constructor function (__init__) from the parent class
        # Employee now uses parent class (Person) but adds its own stuff on
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.account_number = account_number  # Unique to Customer

    def get_account_number(self):
        return self.account_number

    def __add__(self):
        return self.first_name + self.middle_name + self.get_lastname()
