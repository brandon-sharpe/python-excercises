# #1 Conditional Basics
   #1.A)prompt the user for a day of the week, 
    # print out whether the day is Monday or not
is_it_monday = input(f"# 1.A) What day of the week is it? ")
if is_it_monday.lower() == "monday":
    print("   Damn today is Monday!")
else:
    print("    Today is not Monday!")

##1.B) prompt the user for a day of the week,
# print out whether the day is a weekday or a weekend
is_it_the_weekend = input(f"# 1.B) What day of the week is it? ")
if is_it_the_weekend.lower() == "saturday":
    print("    IT'S THE WEEKEND!")
elif is_it_the_weekend.lower() == "sunday":
    print("    IT'S THE WEEKEND!")


else:
    print("   Damn today is a weekday!")
# # 1.C) create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

hours_per_week= 60
hourly_rate =45

if hours_per_week > 40:
    print(f"You made ${(hours_per_week - 40)* hourly_rate*1.5 + 40*hourly_rate} for working {hours_per_week} hours this week, at the rate of ${hourly_rate} an hour")
else:
    print(hours_per_week*hourly_rate)


# # 2Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:


# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

i = 5
while i <= 15:
    print(i)
    i+=1


# Create a while loop that will count by 2's starting
#  with 0 and ending at 100. Follow each number
#  with a new line.

i = 0
while i <=100:
    print(i)
    i+=2

# Alter your loop to count backwards by 
# 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2,
#  and displays the number squared on each 
# line while the number is less than 1,000,000.

i = 2
while i <1000000:
    print(i)
    i = i**2 


# Write a loop that uses print to create
#  the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5

# For Loops

# Write some code that prompts the user for a 
# number, then shows a multiplication table 
# up through 10 for that number.

# For example, if the user enters 7, 
# your program should output:
user_num2 = int(input(" Input a positive number >>"))
for i in range(1,11):
    print (f"{user_num2} x {i} = {user_num2 * i}")

# Create a for loop that uses print to create 
# the output shown below.
for i in range(1,10):
    for j in range(1,i+1):
        print(i,end="")
    print("")


# Prompt the user for an odd number between 1 
#and 50. Use a loop and a break statement to 
# continue prompting the user if they enter 
# invalid input.
#  (Hint: use the isdigit method on strings 
# to determine this). Use a loop and the 
# continue statement to output all the odd 
# numbers between 1 and 50, except for the 
# number the user entered.

skip_this=int(input("Please enter an odd number between 1 and 50 >> "))
while type(skip_this) != int or skip_this % 2 == 0 or skip_this < 1 or skip_this > 50: 
    print("The input provided is not meet the criteria.")
    skip_this=int(input("Please enter an odd number between one and fifty >> "))
    
print("The number you wish to skip is", skip_this)

for i in range (1,51):
    if i % 2 != 0:
        if i == skip_this:
            print("Skipping", i)
            continue
        print("Here is an odd number: ", i)


# The input function can be used to prompt for input and 
# use that input in your python code. Prompt the user to enter
#  a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to 
# convert this to a numeric type.)

pos_num=int(input(" Input a positive number >>"))

while type(pos_num) != int or pos_num <= 0:
    print("This does not meet the criteria")
    pos_num=int(input(" Input a positive number >>"))

for i in range(0,pos_num):
    i+=1
    print(i)

# Write a program that prompts the user for 
# a positive integer. Next write a loop that prints out the numbers 
# from the number the user entered down to 1.

pos_num=int(input(" Input a positive number >>"))

while type(pos_num) != int or pos_num <= 0:
    print("This does not meet the criteria")
    pos_num=int(input(" Input a positive number >>"))

for i in range(0,pos_num):
    i-=1
    print(i)

# One of the most common interview questions for entry-level 
# programmers is the FizzBuzz test. Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range(1,101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    else:
        print (fizzbuzz)

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

user_num=int(input(" Input a number >>"))

print('\nHere is your table!\n')
print('number | squared | cubed')
print('------ | ------- | -----')

for n in range(1, user_num):
    print(f'{n:<7}| {n**2:<8}| {n**3}')

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
grade= int(input(" Input score to be converted to grade. "))

if grade >= 88 and grade <= 100:
    print("A")
elif grade >= 80 and grade <=87:
    print('B')
elif grade >= 67 and grade <= 79:
    print('C')
elif grade >= 60 and grade <= 66:
    print('D')
else:
    print('F')

