# Define a function named is_two. It should 
# accept one input and return True if the 
# passed input is either the number or the 
# string 2, False otherwise.

n = 3
def is_two(n):
    if type(n) == int and n % 2 == 0:
        return True
    elif n == 'two':
        return True
    
    else:
        return False
print (is_two(n))

# Define a function named is_vowel.
#  It should return True if the passed 
# string is a vowel, False otherwise.
letter="E"
vowels =("AEIOUaeiou")
def is_vowel(letter):
    if letter in vowels:
        return True
    else:
        return False
print(is_vowel(letter))

# Define a function named is_consonant. 
# It should return True if the passed string 
# is a consonant, False otherwise. Use 
# your is_vowel function to accomplish this.

def is_constonant(letter):
    if letter not in vowels:
        return True
    else:
        return False
print(is_constonant(letter))

# Define a function that accepts a 
# string that is a word. The function 
# should capitalize the first letter of the 
# word if the word starts with a consonant.

string = "baby"
def cap_word(string):
    if is_constonant(string[0]) == True:
        return string.capitalize()
    else:
        return string
        
print(cap_word("baby"))

# Define a function named calculate_tip.
#  It should accept a tip percentage 
# (a number between 0 and 1) and the bill 
# total, and return the amount to tip.

bill = 100
def calculate_tip(tip):
    tipprec = input("Input a tip precentage between 0 and 1: ")
    if float(tipprec) >= 0 and float(tipprec) <= 1:
        return (float(bill) * float(tipprec)) + float(bill)
print (calculate_tip(bill))

# Define a function named apply_discount. 
# It should accept a original price, and a 
# discount percentage, and return the price 
# after the discount is applied.

def apply_discount(original_price):
    discount_prec = input("Enter discount precentage: ")
    return float(original_price)-(float(original_price) * float(discount_prec)) 
print(apply_discount(100))

# Define a function named handle_commas. 
# It should accept a string that is a number 
# that contains commas in it as input, and 
# return a number as output.

# Define a function named get_letter_grade. 
# It should accept a number and return the 
# letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if type(grade) == int:
        if grade >= 90:
            return "A"
        elif grade >=80:
            return "B"
        elif grade >=70:
            return "C"
        elif grade >=60:
            return "D"
        else:
            return "F"
    else:
        print("please provide a numeric value.")
print(get_letter_grade(70))

# Define a function named remove_vowels that 
# accepts a string and returns a string with 
# all the vowels removed.

def remove_vowel(c):
    return ''.join([l for l in c if l not in vowels])
    
print(remove_vowel("Emily"))

# Define a function named normalize_name. 
# It should accept a string and return a 
# valid python identifier, that is:
# anything that is not a valid python 
# identifier should be removed
# leading and trailing whitespace should 
# be removed
# everything should be lowercase
# spaces should be replaced with underscores

def normalize_name(string):
    return ''.join(ch for ch in string.lower().strip().replace(" ", "_").strip() if ch in "abcdefghijklmnopqrstuvxyz_0123456789")


print(normalize_name("      BrA $$ ndon   "))

# Write a function named cumulative_sum 
# that accepts a list of numbers and 
# returns a list that is the cumulative 
# sum of the numbers in the list.
import numpy
def cumulative_sum(list_of_nums):
    return numpy.cumsum(list_of_nums)

print(cumulative_sum([1,2,3,4]))
    