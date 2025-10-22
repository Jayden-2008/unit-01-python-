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
    
    def balance(owner):
