https://drive.google.com/drive/folders/1v-uAhjIKcurzH9P1GMT9TFDKGWxepirs







from socket import socket
import os
inventory={
    'Laptop':   (10,45000),
    'Mouse':    (85,350),
    'Keyboard': (40,750),
    'Monitor':  (6,12000)
}

total =0
for item,value in inventory.items():
    print(f"Items: {item}, Quantity: {value[0]}, Price: {value[1]}")
    a = value[0]*value[1]
    total +=a
    print("Stock Value: ",a,"\n")
  
a=input("Enter a name")
if a in inventory.keys():
    print("exist")
    price=input("enter a price")
    p=inventory[a][0]
    print(p)
    invent=(p,price)
    inventory[a]=invent
    print(inventory)

for i in inventory.items():
    a=i[1][0]
    print(a)
    if a<8:
        print("critical Stock")
    elif 8<a<12:
        print("low stock")
    elif 21<a<50:
        print("Adequate stock")
    elif a>50:
        print("High stock")

with open("inventory.txt","w") as f:
    for item, value in inventory.items():
        f.write(f"Items: {item}, Quantity: {value[0]}, Price: {value[1]},total :{total}\n")







class Employee:
    organisation_name = "Default Org"

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.salary = salary

    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    @classmethod
    def set_organisation_name(cls, org_name):
        cls.organisation_name = org_name

    def get_employee_details(self):
        return f"ID: {self.emp_id}, Name: {self.name}, 
        Base: {self.base_location}, Deployed: {self.deployed_location}, 
        Desig: {self.designation}, Salary: {self.salary}"

emp_id = input()
name = input()
base_loc = input()
dep_loc = input()
desig = input()
salary = input()

emp = Employee(emp_id, name, base_loc, dep_loc, desig, salary)
print(emp.get_employee_details())





# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes  
class Person:
    def __init__(self, name, place_of_residence):
        self.name = name
        self.place_of_residence = place_of_residence

    def display_attributes(self):
        print(self.name)
        print(self.place_of_residence)

class Sister(Person):
    def __init__(self, name, place_of_residence, exam_subjects):
        super().__init__(name, place_of_residence)
        self.exam_subjects = exam_subjects

    def display_attributes(self):
        super().display_attributes()
        print(self.exam_subjects)

class Uncle(Person):
    def __init__(self, name, place_of_residence, business):
        super().__init__(name, place_of_residence)
        self.business = business

    def display_attributes(self):
        super().display_attributes()
        print(self.business)

if __name__ == "__main__":
    s_name = input()
    s_res = input()
    s_sub = input()
    sister = Sister(s_name, s_res, s_sub)
    sister.display_attributes()

    u_name = input()
    u_res = input()
    u_bus = input()
    uncle = Uncle(u_name, u_res, u_bus)
    uncle.display_attributes()







# Classes and objects -- try creating this in oops world
# Employee
#   # instance variables 
#    emp_id
#    emp_salary(private)
#    mgr_id
#   # class variable 
#   department_name
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary
#   # class method 
#   get_department_name() --> department_name
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
# main
# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary(private)
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects

class Employee:
    department_name = "Engineering"

    def __init__(self, emp_id, emp_salary, mgr_id):
        self.emp_id = emp_id
        self.__emp_salary = emp_salary
        self.mgr_id = mgr_id

    def get_emp_salary(self):
        return self.__emp_salary

    def set_emp_salary(self, rcv_salary):
        self.__emp_salary = rcv_salary

    @classmethod
    def get_department_name(cls):
        return cls.department_name

    @staticmethod
    def field_expertise():
        print("Expertise: Python Development")

if __name__ == "__main__":
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())

    emp = Employee(val1, val2, val3)

    print(emp.emp_id)
    try:
        print(emp.__emp_salary)
    except AttributeError:
        print("Cannot access private variable")
    print(emp.mgr_id)

    print(Employee.get_department_name())
    Employee.field_expertise()

    del emp.mgr_id
    del emp





# Classes and objects -- try creating this in oops world
# library management system
# attributes
# book_name and book_author and cost_price
# # methods
# display book name 
# display book author
# calculate the purchse price of lot of books where a lot(no of books is provided by the user)
# create one book and cost of purchase 10 books
class Book:
    def __init__(self, book_name, book_author, cost_price):
        self.book_name = book_name
        self.book_author = book_author
        self.cost_price = cost_price

    def display_book_name(self):
        print(self.book_name)

    def display_book_author(self):
        print(self.book_author)

    def calculate_purchase_price(self, quantity):
        return self.cost_price * quantity

name = input()
author = input()
price = float(input())
num_books = int(input())

my_book = Book(name, author, price)

my_book.display_book_name()
my_book.display_book_author()
print(my_book.calculate_purchase_price(num_books))



# # class object
# library management system
# instance variable
# book_name and book_author and cost_price( private )
# class variable
# library_name
# library_turnover( private )
# methods
# create a Book
# and try to see its cost_price wheteher it can been seen
# display the library_name
# display the library_turnover # without an error I need it 
# change the library_name with the value provided by the user and display it back
class Library:
    library_name = "City Library"
    __library_turnover = 500000

    def __init__(self, book_name, book_author, cost_price):
        self.book_name = book_name
        self.book_author = book_author
        self.__cost_price = cost_price

    @classmethod
    def get_turnover(cls):
        return cls.__library_turnover

b_name = input()
b_author = input()
b_price = float(input())
new_name = input()

my_book = Library(b_name, b_author, b_price)

try:
    print(my_book.__cost_price)
except AttributeError:
    print("Cannot see private cost_price")

print(Library.library_name)
print(Library.get_turnover())

Library.library_name = new_name
print(Library.library_name)




# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 
class AirlineTicket:
    def __init__(self, departure_city, arrival_city, flight_number, row, seat_letter):
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.flight_number = flight_number
        self.seat_assignment = f"{row}{seat_letter}"

    def display_details(self):
        print(f"Ticket: {self.flight_number}")
        print(f"From: {self.departure_city} To: {self.arrival_city}")
        print(f"Seat: {self.seat_assignment}")
        print("-" * 20)

dep1 = input()
arr1 = input()
f_num1 = input()
row1 = input()
letter1 = input()

dep2 = input()
arr2 = input()
f_num2 = input()
row2 = input()
letter2 = input()

ticket1 = AirlineTicket(dep1, arr1, f_num1, row1, letter1)
ticket2 = AirlineTicket(dep2, arr2, f_num2, row2, letter2)

ticket1.display_details()
ticket2.display_details()






Create program that takes age of the user as input 
and prints number of days that user has lived for 
Exception handle the code such that if the user has lived for more than 
100001 days then user should get the message
, you lived for so long , may be you will die soon:)

# write a program to take some text lines from the user and write it to the file
# write a program to read from a file and write to another file 
# Write a program to read from a file and modify eacf of its line by pre-pending each line with "DIOT-" 
# Write a program to read from a file, pre-pending each line with "DIOT-" 
# and write to the different file
import os
import sys

def main():
    try:
        user_age = input("Enter your age: ")
        total_days = float(user_age) * 365
        print(f"You have lived for approximately {int(total_days)} days.")
        
        if total_days > 100001:
            print("you lived for so long , may be you will die soon:)")
            
    except ValueError:
        print("Error: Invalid numeric input.")
        sys.exit()

    try:
        file_write = input("Enter name for a new file to create: ")
        print("Enter text (type 'DONE' to stop):")
        with open(file_write, 'w') as f:
            while True:
                text = input("> ")
                if text.upper() == 'DONE':
                    break
                f.write(text + "\n")

        file_copy = input(f"Enter filename to copy '{file_write}' into: ")
        with open(file_write, 'r') as fr, open(file_copy, 'w') as fw:
            fw.write(fr.read())

        file_final = input("Enter filename for the final DIOT- version: ")
        with open(file_copy, 'r') as fr, open(file_final, 'w') as fw:
            for line in fr:
                if line.strip():
                    modified = "DIOT-" + line
                    print(f"Processing: {modified.strip()}")
                    fw.write(modified)
                else:
                    fw.write(line)

        print("All operations completed successfully.")

    except FileNotFoundError:
        print("Error: The specified file could not be found.")
    except PermissionError:
        print("Error: Permission denied.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()





# Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 
import sys
def main():
    items = ["Python", "Java", "C++", "JavaScript", "Rust"]
    print(f"The list has {len(items)} elements.")

    try:
        user_input = input("Enter the index (0-4) to see the value: ")
        index = int(user_input)
        print(f"Value at index {index}: {items[index]}")
        
    except (IndexError, ValueError):
        print("Value not found")
        sys.exit()

if __name__ == "__main__":
    main()
