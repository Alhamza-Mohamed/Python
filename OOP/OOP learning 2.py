# Encapsulation 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # private attribute (hidden)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount): 
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
    
acc = BankAccount("Alhamza", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500

acc.__balance = 2000  # Attempt to modify private attribute directly
print(acc.get_balance())  # Output: 1500 (remains unchanged)

# Abstraction
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class StripeProcessor(PaymentProcessor):
    def pay(self, amount):
        print (f"Paid ${amount} using stripe")

# User does not need to know implementation details
payment = StripeProcessor()
payment.pay(100)

    
        

# Inheritance With polymorphism
class Animal:
    def speak(self):
        print ("Animal speaks")

class Dog(Animal):
    def speak(self):
        print ("Bark!")

class Cat(Animal):
    def speak(self):
        print ("Meow!")

dog = Dog()
cat = Cat()

dog.speak()  # Output: Bark!
cat.speak()  # Output: Meow!
#Dog and Cat inhearited the structure from Animal class and provided their own implementation of speak method

# Polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 3.14 * 5**2
    
class Circle(Shape):
    def area (self):
        return 10 * 5
    
shapes = [Rectangle(), Circle()]

for shape in shapes:
    print(shape.area())