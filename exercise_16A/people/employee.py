from exercise_16A.people.person import Person


class Employee(Person):
    # constructor (__init__) with extra parameters to give subclass its own functionality
    # self refers to the current instance of the class
    def __init__(self, firstname, middlename, lastname, email, id_number, department, national_insurance, leave_days=0):
        # use super() to access the constructor function (__init__)  from the superclass (Account)
        super().__init__(firstname, middlename, lastname, email)  # Call the superclass constructor
        # Unique to Employee:
        self.id_number = id_number
        self.department = department
        self.__national_insurance = national_insurance  # __ before to keep it private
        self.leave_days = leave_days

    # polymorphism - this calls the superclass method and adds further information
    def display_info(self):
        base_info = Person.display_info(self)
        return (f"{base_info}"
                f"\nID Number: {self.get_id_number()}"
                f"\nDepartment: {self.get_department()}"
                f"\nNI Number: {self.get_national_insurance()}"
                f"\nLeave Days: {self.get_leave_days()}")

    # getters get the value of an instance attribute, serving as intermediaries
    # they protect the attributes by providing indirect access to modify them
    # can be made non-public (__), worked with indirectly and accessed from outside the class directly through getter
    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    # definitely use a getter as national insurance attribute is private
    # getters don't take arguments, they just return a value
    def get_national_insurance(self):
        # return value of the national insurance instance attribute when the method is called
        return self.__national_insurance

    # operator overloading to add leave days (+ operator)
    def __add__(self, other):
        # add value of other to leave_days attribute of current instance (self)
        self.leave_days += other
        # return current instance after updating leave_days attribute
        return self

    # operator overloading to subtract leave days (- operator)
    def __sub__(self, other):
        # subtract value of other to leave_days attribute of current instance (self)
        self.leave_days -= other
        # return current instance after updating leave_days attribute
        return self

    def get_leave_days(self):
        # return value of the leave_days instance attribute when the method is called
        return self.leave_days
