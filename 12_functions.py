"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print("-----Task 1-----")
print()
print()
#creating a definition that makes names
def user_name(name):
    """
    creates a sentence that says hello to whatever name you type
    """
    print("Hello, " + name + "!")
#put the user name that is being printed with "hello"
user_name("Jayden")

print()
print()
print("-----Task 1-----")
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print("-----Task 2-----")
print()
print()

#creates a definition that squares the value provided
def square(number):
    """
    the objective of this definition is to square the value provided, in this case being 12, and the printing the result
    """
    return number ** 2

x = square(12)

#prints the square of 12
print(x)

print()
print()
print("-----Task 2-----")
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print("-----Task 3-----")
print()
print()
def even_odd(number):
    """
    creates a function in which if the number has a remainder of 0 then it is an even number, 
    but if it has a remainder of 1 then it is odd.
    """
    return number % 2 == 0

#prints one true even statement
print(even_odd(2))
#prints one false odd statement
print(even_odd(7))

print()
print()
print("-----Task 3-----")
"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print("-----Task 4-----")
print()
print()

def area_of_rectangle(w, l):
    """
    creates an equation that multiplies the length of a rectangle
    with the width of the rectangle
    """
    return w * l

#multiplies 6 with 12
area = area_of_rectangle(6, 12)

print(area)

print()
print()
print("-----Task 4-----")
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print('-----Task 5-----')
print()
print()

def celsius_to_fahrenheit(celsius):
    """
    the formula for converting celsius to fahrenheit is 
    9/5 + 32, so i use that equation in order to figure out what the result would
    be
    """
    return (celsius * 9 / 5) + 32

print("Converting celsius to fahrenheit: ")
#converts the celsius temperature 23 into the farenheit temperature 
print(celsius_to_fahrenheit(23))
#converts the celsius temperature 100 into the farenheit temperature 
print(celsius_to_fahrenheit(100))

print()
print()
print('-----Task 5-----')
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print('Task 6')
print()
print()

def calculate_average(numbers):
    """
    adds up all the values in the list and divides it by the amount of 
    values on the list
    """
    return sum(numbers) / len(numbers)

print("The mean of the following values: 10, 20, 30, is")
#calculates the mean of 10, 20 and 30
print(calculate_average([10, 20, 30])) 

print()
print()
print('-----Task 6-----')
"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.
Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""