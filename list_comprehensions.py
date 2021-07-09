
# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and 
# uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax.
#  Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits= [f.upper() for f in fruits]
print()
print ( f"#1:  Make a variable named uppercased_fruits to hold the output of the list comprehension.")
print(uppercased_fruits)
print()

# Exercise 2 - create a variable named capitalized_fruits and 
# use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits=[f.capitalize() for f in fruits]
print(f"#2:  Make a variable named uppercased_fruits to hold the output of the list comprehension.")
print(capitalized_fruits)
print()

# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
vowels = 'aeiouAEIOU'
def more_than_two(f):
    count = 0
    for alphabet in f:
        if alphabet in vowels:
            count = count + 1
            if count > 2:
                return True
two_or_more = [f for f in fruits if more_than_two(f) == True]
print(f"#3: Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.")
print(two_or_more)
print()
#  Exercise 4 - make a variable named fruits_with_only_two_vowels. 
# The result should be ['mango', 'kiwi', 'strawberry']
vowels = 'aeiouAEIOU'
def two_vowels(f):
    count = 0
    for alphabet in f:
        if alphabet in vowels:
            count = count + 1
            if count == 2:
                return True
fruits_with_only_two_vowels= [f for f in fruits if two_vowels(f) == True]
print(f"#4: Make a variable named fruits_with_only_two_vowels.")
print(fruits_with_only_two_vowels)
print()
# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_5=[f for f in fruits if len(f)>5]
print(f"#5: Make a list that contains each fruit with more than 5 characters ")
print(more_than_5)
print()

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
exactly_5=[f for f in fruits if len(f)==5]
print(f"#6: Make a list that contains each fruit with exactly 5 characters")
print(exactly_5)
print()

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
less_than_5=[f for f in fruits if len(f)<5]
print(f"#7: Make a list that contains fruits that have less than 5 characters")
print(less_than_5)
print()

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_letters = [len(f) for f in fruits ]
print(f"#8: Make a list containing the number of characters in each fruit.")
print(number_of_letters)
print()