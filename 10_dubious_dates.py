from datetime import datetime
from datetime import date
from datetime import time
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print("-----Task 1-----")
print()
print()

my_dt = datetime.now()
print(my_dt)

print()
print()
print("-----Task 1-----")

"""

Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print("-----Task 2-----")
print()
print()

my_dt = datetime.now()
print(my_dt)

my_date = datetime.now()
my_string = my_date.strftime("%m/%d/%Y")
print(my_string)

print()
print()
print("-----Task 2-----")

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("-----Task 3-----")
print()
print()

my_string1 = "01/02/2025"
my_string2 = "01/03/2025"
my_date1 = datetime.strptime(my_string1, "%m/%d/%Y")
my_date2 = datetime.strptime(my_string2, "%m/%d/%Y")

name = my_date2 - my_date1
print(my_date1)
print(my_date2)
print("the difference is", name)

print()
print()
print("-----Task 3-----")

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
user_birthdate = input("What is your birthdate in the format (MM/DD/YYYY)?: ")
my_date = datetime.strptime(user_birthdate, "%m/%d/%Y")
current_time = datetime.now()
difference = current_time - my_date

print(difference)
