'''
Q1. Types of Methods – Instance, Class, Static
Define a class Student with:
● An instance method display() to show name and age
● A class method get_total_students() to count student objects
● A static method is_eligible(age) to check if age is between 18 and 30
Input:

s1 = Student("Arun", 20)
s2 = Student("Meena", 17)
s1.display()
Student.get_total_students()
print(Student.is_eligible(25))

Output:

Name: Arun, Age: 20
Total Students: 2
True
'''
class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1


    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def get_total_students(cls):
        print(f"Total Students: {cls.total_students}")

    @staticmethod
    def is_eligible(age):
        return 18 <= age <= 30


s1 = Student("Arun", 20)
s2 = Student("Meena", 17)
s1.display()
Student.get_total_students()
print(Student.is_eligible(25))
'''
Q2. Constructor Usage
Create a class Book that uses a constructor to initialize:
● title
● author
● price
Add a method display_info().

Python

Python

Python

Python
Input:

b = Book("The Alchemist", "Paulo Coelho", 299)
b.display_info()

Output:

Title: The Alchemist
Author: Paulo Coelho
Price: ₹299
'''
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")


b = Book("The Alchemist", "Paulo Coelho", 299)
b.display_info()
'''
Q3. Encapsulation – Public, Protected, Private
Create a class Account:
● Public: account_holder
● Protected: _balance
● Private: __pin
Add methods:
● deposit(amount)
● withdraw(pin, amount)
● show_balance()
Input:

acc = Account("Ravi", 1234)
acc.deposit(5000)
acc.withdraw(1234, 1500)
acc.show_balance()

Output:

Deposited ₹5000
Withdrawn ₹1500
Available Balance: ₹3500
'''
class Account:
    def __init__(self, account_holder, pin):
        self.account_holder = account_holder
        self._balance = 0
        self.__pin = pin

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawn ₹{amount}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN")

    def show_balance(self):
        print(f"Available Balance: ₹{self._balance}")


acc = Account("Ravi", 1234)
acc.deposit(5000)
acc.withdraw(1234, 1500)
acc.show_balance()
'''
Q4. Multilevel Inheritance – Ride Booking System
Create classes:
● User → method: login()
● Rider(User) → method: book_ride()
● Payment(Rider) → method: make_payment()
Input:

p = Payment()
p.login()
p.book_ride()
p.make_payment()

Output:

User logged in
Ride booked successfully
Payment completed
'''
class User:
    def login(self):
        print("User logged in")

class Rider(User):
    def book_ride(self):
        print("Ride booked successfully")

class Payment(Rider):
    def make_payment(self):
        print("Payment completed")


p = Payment()
p.login()
p.book_ride()
'''
Q5. Multiple Inheritance – Food Delivery App
Create:
● LocationService → method: track_location()
● OrderService → method: place_order()
● DeliveryApp(LocationService, OrderService) → method:
confirm_delivery()
Input:

app = DeliveryApp()
app.track_location()
app.place_order()
app.confirm_delivery()

Output:

Current location tracked
Order placed successfully
Delivery confirmed to your address
'''
class LocationService:
    def track_location(self):
        print("Current location tracked")

class OrderService:
    def place_order(self):
        print("Order placed successfully")

class DeliveryApp(LocationService, OrderService):
    def confirm_delivery(self):
        print("Delivery confirmed to your address")

app = DeliveryApp()
app.track_location()
app.place_order()
app.confirm_delivery()
'''
Q6. Hierarchical Inheritance
Create base class Employee with method show_name().
Create subclasses:
● Manager → manage_team()
● Developer → write_code()
Input:

m = Manager("Vikram")
d = Developer("Anjali")
m.show_name()
m.manage_team()
d.show_name()
d.write_code()

Output:

Employee Name: Vikram
Managing team...
Employee Name: Anjali
'''
class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Employee Name: {self.name}")

class Manager(Employee):
    def manage_team(self):
        print("Managing team...")

class Developer(Employee):
    def write_code(self):
        print("Writing code...")


m = Manager("Vikram")
d = Developer("Anjali")
m.show_name()
m.manage_team()
d.show_name()
d.write_code()
'''
Q7. Using super()
Base class: Person(name, age)
Derived class: Teacher(name, age, subject)
Use super() in constructor and create method show().
Input:

t = Teacher("Suma", 35, "Math")
t.show()

Output:

Name: Suma, Age: 35, Subject: Math
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")


t = Teacher("Suma", 35, "Math")
t.show()
'''
Q8. Class Variables vs Instance Variables
Create a class Company:
● Class variable: company_name
● Instance variables: employee_name, salary
Add method display().
Input:

e1 = Company("Rahul", 50000)
e2 = Company("Neha", 60000)
e1.display()
e2.display()

Output:

Company: TechCorp
Employee: Rahul, Salary: 50000
Company: TechCorp
Employee: Neha, Salary: 60000
'''
class Company:
    company_name= 'TechCorp'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f'Company: {Company.company_name}\nEmployee: {self.name}, Salary: {self.salary}')


e1 = Company("Rahul", 50000)
e2 = Company("Neha", 60000)
e1.display()
e2.display()
'''
Q9. Class Method vs Static Method (NEW)
Create a class Exam with:
● Class variable pass_mark = 40
● Class method change_pass_mark(new_mark)
● Static method is_pass(score) that returns True if score ≥ pass_mark
Input:

Exam.change_pass_mark(50)
print(Exam.is_pass(45))
print(Exam.is_pass(55))

Output:

False
True
'''
class Exam:
    pass_mark = 40

    @classmethod
    def change_pass_mark(cls,new_mark):
        cls.pass_mark = new_mark

    @staticmethod
    def is_pass(score):
        return score >= Exam.pass_mark


Exam.change_pass_mark(50)
print(Exam.is_pass(45))
print(Exam.is_pass(55))
'''
Q10. Object Composition – Car & Engine
Create:
● Engine class with method start_engine()
● Car class that has an Engine object and method start_car()

Python

None
Input:

car = Car()
car.start_car()

Output:

Engine started
Car is running
'''
class Engine:
    def start_engine(self):
        print("Engine started")

class Car(Engine):
    def start_car(self):
        self.start_engine()
        print('Car is running')


car = Car()
car.start_car()
