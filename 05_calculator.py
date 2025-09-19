print("Hello, wwelcome to my personal calculator!")

number_1 = float(input("Please enter the first number: "))
number_2 = float(input("Please enter the second number: "))


print("Select Operation: ")
print("1. Addition")
print("2. Subraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponents")
print("7. Remainder")

choice = input("Please enter which operation you would like to use: ")


if choice == "1":
    Addition = number_1 + number_2
    print(Addition)
elif choice == "2":
    Subtraction = number_1 - number_2
    print(Subtraction)
elif choice == "3":
    Multiplication = number_1 * number_2
    print(Multiplication)
elif choice == "4":
    if number_2 > 0 or number_2 < 0:
        Division = number_1 / number_2
        print(Division)
    else:
        print("Cannot calculate that number.")
elif choice == "5":
    Floor_Division = number_1 // number_2
    print(Floor_Division)
elif choice == "6":
    Exponents = number_1 ** number_2
    print(Exponents)
elif choice == "7":
    Remainder = number_1 % number_2
    print(Remainder)
else:
    print("Syntax Error, please try again.")

