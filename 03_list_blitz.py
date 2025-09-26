"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
# ------Task 1------
# Create a list with 4 elements and print it.

print("------Task 1------")
print()
print()

# Creating a list with 4 fruit items
my_list = ["apple", "banana", "cherry", "date"]

# Printing the list
print(my_list)

print()
print()
print("------Task 1------")


# ------Task 2------
# Add an element to the end of the list and print the updated list.

print("------Task 2------")
print()
print()

# Reinitializing the list (optional but makes sure it starts fresh)
my_list = ["apple", "banana", "cherry", "date"]

# Adding a new item to the end of the list
my_list.append("cranberry")

# Printing the updated list
print(my_list)

print()
print()
print("------Task 2------")


# ------Task 3------
# Remove a specific element from the list and print the updated list.

print("------Task 3------")
print()
print()

# Printing the current list before removal
print(my_list)

# Removing the element "banana" from the list
my_list.remove("banana")

# Printing the updated list
print(my_list)

print()
print()
print("------Task 3------")


# ------Task 4------
# Modify an element at a specific index and print the updated list.

print("------Task 4------")
print()
print()

# Printing the current list before modification
print(my_list)

# Replacing the element at index 1 with "blueberry"
my_list[1] = "blueberry"

# Printing the updated list
print(my_list)

print()
print("------Task 4------")


# ------Task 5------
# Append multiple elements to the end of the list and print the updated list.

print("------Task 5------")
print()
print()

# Printing the list before extending
print(my_list)

# Adding multiple new fruits to the list at once
my_list.extend(["elderberry", "fig", "grape"])

# Printing the updated list
print(my_list)

print()
print("------Task 5------")


# ------Task 6------
# Delete an element at a specific index and print the updated list.

print("------Task 6------")
print()
print()

# Printing the list before deletion
print(my_list)

# Deleting the element at index 2
del my_list[2]

# Printing the updated list
print(my_list)

print()
print()
print("------Task 6------")


# ------Task 7------
# Create a new variable that holds the first 2 items of the list (slicing).

print("------Task 7------")
print()
print()

# Printing the full list
print(my_list)

# Creating a new variable that holds the first two elements
new_variable = my_list[0:2]

# Printing the new variable
print(new_variable)

print()
print()
print("------Task 7------")


# ------Task 8------
# Extend the list with another list and print the updated list.

print("------Task 8------")
print()
print()

# Printing the list before final extension
print(my_list)

# Extending the list with two new elements
my_list.extend(["honeydew", "kiwi"])

# Printing the final list
print(my_list)

print()
print()
print("------Task 8------")