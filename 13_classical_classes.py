"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print("-----Task 1-----")
print()
print()

#the class will allow the computer to print the name and age of the person chosen by me
class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name

jayden = Person('Jayden', 17)
print(jayden.name)
print(jayden.age)

print()
print()
print("-----Task 1-----")
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print('-----Task 2-----')
print()
print()

#main class that allows the animals to speak 
class Animal:

    def speak(self):
        print('This animal can speak')

#subclass 1 which allows the dog to go woof
class Dog(Animal):

    def speak(self):
        print('The dog goes woof')

#prints the speaak variable that allows the dog to go woof
dog = Dog()
dog.speak()

#subclass 2 which allows the cat to go meow
class Cat(Animal):

    def speak(self):
        print('The cat goes meow')
 
#prints the speak variable which allows the cat to go meow
cat = Cat()
cat.speak()


print()
print()
print('-----Task 2-----')
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

print('-----Task 3-----')
print()
print()

class BankAccount:
    def __init__(self, owner, balance=0):
        """Initialize a new bank account."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount: }. New balance: ${self.balance: }")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount: }. New balance: ${self.balance: }")

    def __str__(self):
        """Return a string representation of the account."""
        return f"BankAccount(owner: {self.owner}, balance: ${self.balance: })"

account1 = BankAccount("Jayden", 1000)
account2 = BankAccount("Liam", 500)

# Test deposits
account1.deposit(200)
account2.deposit(300)

# Test withdrawals
account1.withdraw(150) 
# Should show insufficient funds
account2.withdraw(900) 

# Display final account info
print()
print(account1)
print()
print(account2)

print()
print()
print('-----Task 3-----')