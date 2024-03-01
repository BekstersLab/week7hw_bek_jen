from people.person import Person


class Employee(Person):
    def __init__(self, firstname, middlename, lastname, email, id_number, department, leave_days):
        # use super() to refer to the base or parent class
        # in this case we use super() to access the __init__ method from the Person class
        # calls the constructor function (__init__) from the parent class
        # Employee now uses parent class (Person) but adds its own stuff on
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.id_number = id_number  # Unique to Employee
        self.department = department  # Unique to Employee
        self.leave_days = leave_days

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def __add__(self, other):
        if isinstance(other, (int, float)) and self.leave_days + other >= 0:
            self.leave_days += other
        else:
            print("Error")
        return self










