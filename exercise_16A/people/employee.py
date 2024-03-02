from exercise_16A.people.person import Person


class Employee(Person):
    def __init__(self, firstname, middlename, lastname, email, id_number, department, national_insurance, leave_days=0):
        # use super() to refer to the base class
        # in this case we use super() to access the __init__ method from the Person class
        # calls the constructor function (__init__) from the parent class
        # Employee now uses parent class (Person) but adds its own stuff on
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.id_number = id_number  # Unique to Employee
        self.department = department  # Unique to Employee
        self.__national_insurance = national_insurance
        self.leave_days = leave_days

    # polymorphism - this calls the base class method and adds further information
    def display_info(self):
        base_info = Person.display_info(self)
        return (f"{base_info}"
                f"\nID Number: {self.get_id_number()}"
                f"\nDepartment: {self.get_department()}"
                f"\nNI Number: {self.get_national_insurance()}"
                f"\nLeave Days: {self.get_leave_days()}")

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_national_insurance(self):
        return self.__national_insurance

    def __add__(self, other):
        self.leave_days += other
        return self

    def __sub__(self, other):
        self.leave_days -= other
        if self.leave_days < 0:
            self.leave_days = 0
        return self

    def get_leave_days(self):
        return self.leave_days
