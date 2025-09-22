"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
# A simple print that sections each task
print("------Task 1------")
print()
print()

# Using variable i, setting it to 1 as the starting point
i = 1
#the while function will activate as long as i is less than 11 
while i < 11:
# This will simply print i
    print(i)
#i will increase as long as it is greater or equal to 1, until it gets to 10
    i += 1


print()
print()
print("------Task 1------")
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print("------Task 2------")
print()
print()

#The starting point of i will be 10
i = 10
#will activate as long as i is greater than 0, until it reaches 10
while i > 0:
    # print the variable i
    print(i)
    # i will decrease by 1 each time from 10 until it reaches 1
    i -= 1


print()
print()
print("------Task 2------")
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print("------Task 3------")
print()
print()

#the number variable will ask the user for a number
number = int(input("Give me a number: "))
#the result will make sure that it will print to end result
result = 1

#while the number variable that the user chooses is greater than zero, it will print the number that they choose
while number > 0:
    print(number)
    print()
    #set the number as a factorial, where it will do the number the user chooses, times the result
    result = number * result
    #the number from number times result will decrease the factor of number by one each time
    number -= 1
#this will continue to print the result until it reaches one
print(result)

print()
print()
print("------Task 3------")
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print("------Task 4------")
print()
print()

#the password that I set for the user to guess
password = "Jayden08"
#this will allow the user to enter their attempt of what they think the password is
user_attempt = ""

print("Welcome to the password guessing game!")

#while the users guess is incorrect, the code will continue to ask them to enter the password again
while user_attempt != password:
    user_attempt = input("Enter your password: ")
#once the user guesses the password, the code run will end since they got it correct
else:
    print("You got it!")


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""