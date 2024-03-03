from people.person import Person
from people.employee import Employee
from people.customer import Customer

person_1 = Person('Mary', 'Alice', 'Peterson', 'mary.peterson@gmail.com')

person_firstname = person_1.get_firstname()
person_middlename = person_1.get_middlename()
person_lastname = person_1.get_lastname()
person_email = person_1.get_email()

print(f"{person_firstname} {person_lastname}'s email address is {person_email}")
# Mary Peterson's email address is mary.peterson@gmail.com

# create an instance of Employee class
r_jones = Employee('Robert', 'Edward', 'Jones', 'robert.jones@gmail.com',
                   'EM4505', 'sales', 'JB 56 73 80 C', 20)

# instance (r_jones) - call getter to get value and assign to a variable
# the variables can then be referenced in an f-string to print
employee_firstname = r_jones.get_firstname()
employee_middlename = r_jones.get_middlename()
employee_lastname = r_jones.get_lastname()
employee_email = r_jones.get_email()
employee_id = r_jones.get_id_number()
employee_department = r_jones.get_department()
employee_national_insurance = r_jones.get_national_insurance()
employee_leave_days = r_jones.get_leave_days()

# initially started calling the defined variables above...
print(f"{employee_firstname} {employee_middlename} {employee_lastname} works in the {employee_department} department")
# Robert Edward Jones works in the sales department

print(f"{employee_firstname}'s employee ID number is {employee_id} and his national insurance number is "
      f"{employee_national_insurance}")
# Robert's employee ID number is EM4505 and his national insurance number is JB 56 73 80 C

# changed way of referencing variable, now use instance variable name with the method from employee.py
print(f"{r_jones.first_name} {r_jones.get_lastname()} has {r_jones.leave_days} leave days remaining")
# Robert Jones has 20 leave days remaining

# using the overload add operator to add leave days to existing amount
r_jones + 6
print(f"{r_jones.first_name} now has {r_jones.leave_days} leave days remaining")
# Robert now has 26 leave days remaining

# using the overload subtract operator to deduct leave days
r_jones - 30
# taking more leave than remaining shows 0.
# this could be fixed to give an error message if he takes more than remaining amount
print(f"{r_jones.first_name} has {r_jones.leave_days} leave days remaining")
# Robert has 0 leave days remaining

# set a generic variable to reference each employees information as defined in display_info method
employee_display_info = r_jones.display_info()
# polymorphism - printing info using display_info method from Employee class
print(f"{employee_display_info}")
# Name: Robert Edward Jones - from display_info in Person class
# Email: robert.jones@gmail.com - from display_info in Person class

s_harris = Employee('Sarah', 'Louise', 'Harris', 'sarah.harris@gmail.com',
                    'EM0306', 'accounts', 'GE 56 38 61 D', 5)

# reassign the variable with a new instance (s_harris)
employee_display_info = s_harris.display_info()
print(f"{employee_display_info}")

# DO NOT USE - incorrect use of operator overloading
# customer_1 = Customer('Helen', 'Claire', 'Herbert', 'helen.herbert@gmail.com', '85647239')
# # use __add__ in customer.py to join attributes together into one variable which is easier to call
# customer_fullname = customer_1.first_name + " " + customer_1.middle_name + " " + customer_1.get_lastname()
# customer_account = customer_1.get_account_number()
# print(f"{customer_fullname}'s account number is: {customer_1.get_account_number()}")

print('\n', '~' * 15, 'CUSTOMER SUB CLASS', '~' * 15)
# CUSTOMER SUB CLASS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OBJECT 1

# An object of the Customer subclass is instantiated with 5 arguments, object is assigned to customer1
customer1 = Customer('Mei', 'Ling', 'Chen', 'mei.chen@example.com', '01221234')

customer1.set_total_purchase(500.523)  # sets the total amount spent in the customer1 object

print(customer1)  # prints customer1 object, based on method overriding behaviour for special str method

# prints the total amount spent by the customer1 object
print(f'Purchase Total: £{customer1.get_purchase_total()}\n')

# OBJECT 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Another object of the Customer subclass is instantiated with 5 arguments, object is assigned to customer2
customer2 = Customer('Emily', 'Anne', 'Smith', 'emily.smith@example.com', '9876543210')

customer2.set_total_purchase(212.31)  # sets the total amount spent in the customer2 object

print(customer2)  # prints customer2 object, based on method overriding behaviour for special str method

# prints the total amount spent by the customer2 object
print(f'Purchase Total: £{customer2.get_purchase_total()}\n')

# + operator overloading behaviour is applied on two objects, customer1 and customer
# prints a string containing a sum of two objects' total purchases
print(f'Sum of two object\'s total purchases: £{customer1 + customer2}\n')

# OBJECT 3 - Testing Try and Except block for TypeError ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Another object of the Customer subclass is instantiated with 5 arguments, object is assigned to customer3
customer3 = Customer('Michael', 'A', 'Scott', 'm.scott@example.com', '5629473801')

customer3.set_total_purchase('678')  # testing if Except block will print a string, informing user of TypeError

# prints the total amount spent by the customer3 object, £0 due to exception encountered
print(f'Purchase Total: £{customer3.get_purchase_total()}\n')
