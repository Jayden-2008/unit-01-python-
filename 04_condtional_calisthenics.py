'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

# Prompt the user to input a number and convert it to an integer

x = int(input("Pick any number"))

# Check if the number is less than 10

if x < 10:
    print('x is not 10')  # If x is less than 10, print this message

# Check if the number is greater than 10

elif x > 10:
    print('x is not 10') # If x is greater than 10, print this message

# If x is neither less than nor greater than 10, it must be equal to 10

else:
    print('x is 10') # Print this message when x is exactly 10

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = int(input("What is your age?"))
student = (input("Are you a student?: Yes or No"))

if age < 18 or student == "Yes":
    print('Your ticket is $10')

else:
    print('Your ticket will cost $20')

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

ask_fruit = (input("Pick a fruit : Apple , Orange, Strawberry"))

x = {
    "Apple", 
    "Orange",
    "Strawberry"
}

if ask_fruit in x:
    print('Yes, that fruit is in the lis.')
else:
    print("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''