"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""

print("-----Task 1-----")
print()
print()
#creating the random module that we will need for all tasks
import random
# Simulate rolling a six-sided die 10 times
for i in range(10):
    roll = random.randint(1, 6)
# Print each roll result
    print(f"Roll {i+1}: {roll}")
print()

print()
print()
print("-----Task 1-----")

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print("-----Task 2-----")
print()
print()

# 5 floats between 0 and 1
for i in range(5):
    num1 = random.uniform(0, 1)
    print(f"Random float between 0 and 1: {num1}")
# 5 floats between 10 and 20
for i in range(5):
    num2 = random.uniform(10, 20)
    print(f"Random float between 10 and 20: {num2}")

print()
print()
print("-----Task 2-----")

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print("-----Task 3-----")
print()
print()

# List of colors
colors = ["red", "blue", "green", "yellow", "purple"]
# Randomly select 3 colors without replacement
selected_colors = random.sample(colors, 3)
# Print the selected colors
for color in selected_colors:
    print(f"Selected color: {color}")

print()    
print()
print("-----Task 3-----")

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print("-----Task 4-----")
print()
print()

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
# Shuffle the list
random.shuffle(numbers)
# Print the shuffled result
print("Shuffled numbers:", numbers)

print()
print()
print("-----Task 4-----")




