"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
print("------TASK 1------")
print()
print()

my_float = 12.78
my_int = int(my_float)
print("Original float:", my_float)
print("Converted integer:", my_int)

print()
print()
print("------TASK 1------")
print()

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.

"""
print("------Task 2------")
print()
print()

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print()
print()
print("------Task 2------")
print()

"""

TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

print("------TASK 3------")
print() 
print()

int_num = int(input("Enter an integer: "))
float_num = float(input("Enter a float: "))
Addition = {int_num} + {float_num} 
print(Addition)
Subtraction = int_num - float_num
print(Subtraction)
Multiplication = int_num * float_num
print(Multiplication)
Division = {int_num} / {float_num}
print(Division)

print()
print()
print("------TASK 3------")
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""