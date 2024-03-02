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

    def get_email(self):
        return self.email

    # other refers to another object of this class
    def __add__(self, other):
        return (f'Fullname: {self.first_name} {self.middle_name} {self.__last_name}\nEmail: {self.email}\n\n'
                f'Fullname: {other.first_name} {other.middle_name} {other.__last_name}\nEmail: {other.email}')


if __name__ == '__main__':

    # instantiated 2 objects of the Person class
    person_a = Person('Emily', 'Grace', 'Thompson', 'emily.thompson@example.com')
    person_b = Person('Alexander', 'James', 'Rodriguez', 'alexander.rodriguez@example.com')

    print(person_a + person_b)
