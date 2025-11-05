#Unidirectional Association

class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name
    
    def teach(self, student):
        print(f"{self.name} is teaching {student.name}")    

teacher = Teacher("Omar")
student = Student("Mohamed")

teacher.teach(student) 

#Bidirectional Association
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        book.author = self

class Book:
    def __init__(self, title):
        self.title = title
        self.author = None #Every Book object has an author attribute, even if it starts empty.

author = Author("Alhamza")
book1 = Book("OOP")

author.add_book(book1)
print(f"Author: {book1.author.name}, Book: {book1.title}")

#Aggregation with a list of objects
class Employee:
    def __init__(self, name, role ):
        self.name = name
        self.role = role


    def __repr__(self):#Python doesn’t know which attributes you want to show — it only knows your object exists in memory.
        return f"Employee(Name is '{self.name}', role is '{self.role}')"#By defining __str__ or __repr__, you’re teaching Python how to describe your object in a readable way.

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = [] # aggregation relationship with list: holds Employee objects

    def add_employee(self, employee):
        self.employees.append(employee) 
    
    def show_employees(self):
        for emp in self.employees:
            print(f"{emp.name} has role {emp.role}")


emp1 = Employee("Alhamza", "AI Engineer")
emp2 = Employee("Mohamed", "ML Engineer")

department1 =  Department("AI Deparnment")

department1.add_employee(emp1)
department1.add_employee(emp2)


print(department1.employees) 


#Aggregation with an object
class Engine:
    def __init__(self, name):
        self.name = name 
    def __repr__(self):
        return self.name
class Car:
    def __init__ (self, brand, engine_name):
        self.brand = brand
        self.engine = engine_name #aggrigation with object

engin1 = Engine("v6")
car1 = Car("Toyota",engin1)

print(f"the car's brand is {car1.brand} and its engin is {car1.engine.name}")

# Composition
class Engine_power:
    def __init__(self,horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started")
        
class vehicle:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine_power(horsepower) # created INSIDE → composition
    
    def start(self):
        print (f"{self.brand} car started")
        self.engine.start()

car3 = vehicle("Toyota", 500)
car3.start()

# Dependency 
class Mechanic:
    def repair(self, truck):
        print(f"Repairing {truck.brand} Done")

class Truck:
    def __init__(self,brand):
        self.brand = brand
    
    def service(self, mechanic): # depends on Mechanic
        mechanic.repair(self)    # uses Mechanic temporarily

truck1 = Truck("Mercedes")
mechanic1 = Mechanic()

truck1.service(mechanic1) # it calls mechanic1.repair(truck1)
