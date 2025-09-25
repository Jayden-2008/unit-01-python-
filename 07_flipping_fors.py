"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print("------Task 1------")
print()
print()

#this is the variable that i will be using for this excercsie 
animal = "Duck"

#for each character in duck, we will print out each individual letter
for char in animal:
    print(char)


print()
print()
print("------Task 1------")

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print("------Task 2------")
print()
print()

#this is the number values that will we be using in this excercise
numbers = [1, 10, 30]
#we will begin the total at 0
total = 0

#for each num in numbers the computer will add each number to the total value that begins at zero
for num in numbers:
    total += num

#this will print of the total of the elements in the list
print("The sum of the elements in the list is: ", total)

print()
print()
print("------Task 2------")
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print("------Task 3------")
print()
print()
#this is the example sentence 
sentence = "Shaniya said my mom stinks"

#the variable word will cause the system to split the sentence up into a list of each word
words = sentence.split()

#for each word in words, it will print the word as the amount of letters in it
for x in words:
    print(len(x))

print()
print()
print("------Task 3------")
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print("------Task 4------")
print()
print()

#the dictionary that I created
about_me = {
    "name": "Jayden",
    "age": 17,
    "favorite_game": "Roblox",
    "game_console": "PlayStation"
}
#for each key and value in the items, it will print the key and value in the pair
for key, value in about_me.items():
    print(key, value)

#The computer ends up printing the value without the key, however I found a way around it