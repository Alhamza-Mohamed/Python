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