# Display a welcome message to the user
print("Hello, wwelcome to my personal calculator!")  # Note: "wwelcome" has a typo

# Prompt the user to input the first number and convert it to a float
number_1 = float(input("Please enter the first number: "))

# Prompt the user to input the second number and convert it to a float
number_2 = float(input("Please enter the second number: "))

# Display available operations
print("Select Operation: ")
print("1. Addition")
print("2. Subtraction")  
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponents")
print("7. Remainder")

# Ask the user to choose an operation by number (as a string)
choice = input("Please enter which operation you would like to use: ")

# Check the user's choice and perform the corresponding operation

if choice == "1":
    # Addition
    Addition = number_1 + number_2
    print(Addition)

elif choice == "2":
    # Subtraction
    Subtraction = number_1 - number_2
    print(Subtraction)

elif choice == "3":
    # Multiplication
    Multiplication = number_1 * number_2
    print(Multiplication)

elif choice == "4":
    # Division with check to prevent division by zero
    if number_2 > 0 or number_2 < 0:  
        Division = number_1 / number_2
        print(Division)
    else:
        print("Cannot calculate that number.")  # Error message for division by zero

elif choice == "5":
    # Floor Division
    if number_2 > 0 or number_2 < 0:
        Floor_Division = number_1 // number_2
        print(Floor_Division)
    else:
        print("Cannot calculate that number.")  # Error message for division by zero

elif choice == "6":
    # Exponents
    Exponents = number_1 ** number_2
    print(Exponents)

elif choice == "7":
    # Remainder (modulus)
        if number_2 > 0 or number_2 < 0:
            Remainder = number_1 % number_2
            print(Remainder)
        else:
            print("Cannot calculate that number.")  # Error message for division by zero


else:
    # Handle invalid input
    print("Syntax Error, please try again.")