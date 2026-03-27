class Car: #class definition
    def __init__(self, color, brand): #constructor method
        self.color = color
        self.brand = brand
    
    def drive(self):#method definition
        print(f"The {self.color} {self.brand} is driving.")

    
car1 = Car("red", "Toyota") #car1 is an instance (object) of class Car "red" is an attribute value for color 
car2 = Car("blue", "BMW")


car1.drive()#method call
car2.drive()

car1.color = "green" #modifying attribute value
car1.drive()


class MathUtils:
    pi = 3.1415 #class variable (static Attributes)

    @staticmethod
    def add(a, b): #static method
        return a + b
    
print(MathUtils.pi) #accessing class attribute
result = MathUtils.add(5, 7) #calling static method
print(f"Addition Result: {result}")

class Student:
    school = "AI Academy" #class variable

    def __init__(self, name, grade, department): #constructor method
        self.name = name
        self.department = department 
        self.grade = grade

    def study(self):
        print(f"{self.name} is studding in {self.school}. He is in {self.department} department and his grade is {self.grade}.")

#create objects
s1 = Student("Alhamza","A","Computer Engineering")
s1.study()
print (s1.school)

# Dependency 
class EmailService:
    def send (self, message):
        print (f"Sending email: {message}" )

class OrderProcessor:
    def __init__ (self, email_service: EmailService): # dependency injected here
        self.email_service = email_service            # stored as an instance attribute

    def process(self, order):  
        print (f"Processing order: {order}")
        self.email_service.send (f"order {order} confirmed!")

service = EmailService()                # create the dependency
processor = OrderProcessor (service)    # inject in into the constructor
processor.process("ORD-001")