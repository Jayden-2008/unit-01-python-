"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

print('--Task 1--')
def divide_numbers(num1, num2):
    try: 
        # Try to perform division
        result = num1 / num2
    except ZeroDivisionError:  
        # Handle case where denominator is zero
        print("You cannot divide by zero")

# Example usage:
divide_numbers(10, 0)
print("--Task 1--")

"""
Example 2: Opening Files
"""
print('--Task 2--')

def read_file(filename):
    try: 
        # Try to open the file in read mode
        file = open(filename, 'r')
        # Read the contents of the file
        contents = file.read()
        # Print the file contents
        print("File contents:", contents)
        # Close the file after reading
        file.close()
    except FileNotFoundError: 
        # Handle when the file does not exist
        print('this file has not been created.')

# Example usage:
read_file("nonexistent.txt")

print('--Task 2--')

"""
Example 3: List Items
"""

print('--Task 3--')

def get_item(lst, index):
    try:
        # Try to access the list element at the specified index
        item = lst[index]
        print("Item:", item)
    except IndexError:
        # Handle case where the index is out of range
        print('Index is out of range')

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

print('--Task 3--')

"""
Example 4: Dictionaries
"""

print('--Task 4--')

def get_value(dictionary, key):
    try:
        # Try to access the dictionary value using the provided key
        value = dictionary[key]
        print("Value:", value)
    except KeyError:
        # Handle case where the key does not exist in the dictionary
        print('This value does not exist')

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

print('--Task 4--')

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""

print('--Task 5--')

def process_file(filename):
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        # Handle case where the file cannot be found
        print("Error: File not found.")
    else: 
        # Execute if no exceptions occur
        print('This file has been created')

# Example usage:
process_file("example.txt")

print('--Task 5--')