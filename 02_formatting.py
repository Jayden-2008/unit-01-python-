"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
print("------Task 1------")
print()
print()
my_var = "correct_password"
correct_password = "SecurePass123"
user_input = input("Enter your password: ")
if user_input.lower() == correct_password.lower():
    print("Access granted.")
else:
    print("Access denied. Incorrect password.")

print()
print()
print("------Task 1------")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

print("------Task 2------")
print()
print()
user_input = input("Enter something: ")
if user_input.strip() == "":
    print("invalid")
else:
    print("valid")

print()
print()
print("------Task 2------")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 

"""

text = input("Enter a sentence: ")
my_var = "dog"
dog = text.replace("cat", "dog")

print(dog)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = str(input("what is your name?"))
age = int(input("what is your age?"))

print(name + " " + str(age))
"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
float_user = FloatingPointError("give me a float")
float_user2 = float("Give ma another float")
if float_user2 != 0:
    answers = float_user/float_user2
    rounded_answer = round(answers, 1)
    print("The answer is:", rounded_answer)
else:
    print("there is an error")