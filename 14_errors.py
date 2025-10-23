"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print("Task 1:")
def divide_numbers(num1, num2):
    try: 
        result = num1 / num2
    except ZeroDivisionError:  
        print("You cannot divide by zero")

# Example usage:
divide_numbers(10, 0)
print("--Task 1--")

"""
Example 2: Opening Files
"""

def read_file(filename):
    try: 
        file = open(filename, 'r')
    except FileNotFoundError: 
        print('this file has not been created.')
    contents = file.read()
    print("File contents:", contents)
    file.close()

# Example usage:
read_file("nonexistent.txt")

