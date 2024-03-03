# classes are blueprints or recipes that we can later use to create objects from
# a class describes what properties and functionality individual objects will contain
# use a class to create individual instances (objects) made from that blueprint (class) - instance of class
# class name always starts with a capital letter

# inheritance - shared attributes all have
# define a class (Person) that has the base; firstname, middlename, lastname, email
# Employee and Customer will inherit from user but have their own attributes

class Person:
    # __init__ is a special method called the CONSTRUCTOR which starts/ends in dunderscore - it is special
    # anything inside it will be called when we create a new Person
    # Person is a pattern, __init__ is a method called when we instantiate a new Person
    def __init__(self, firstname, middlename, lastname, email):
        self.first_name = firstname
        self.middle_name = middlename
        self.__last_name = lastname
        self.email = email

    # instance method - it can know about each different instance of Person and access different properties on self
    def get_firstname(self):
        return self.first_name

    def get_middlename(self):
        return self.middle_name

    def get_lastname(self):
        return self.__last_name

    def get_fullname(self):
        return f"{self.first_name} {self.middle_name} {self.__last_name}"

    def get_email(self):
        return self.email

    # polymorphism - Employee will override this method to add specific information only relevant to employees
    def display_info(self):
        return (f"***************************"
                f"\nName: {self.get_fullname()}"
                f"\nEmail: {self.email}")

    # # bad code - first experiment with overloading + operator, but used incorrectly
    # # replaced with get_fullname method above
    # def __add__(self):
    #     return self.first_name + self.middle_name + self.get_lastname()
