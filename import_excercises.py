import test_functions ## test functions is where I stored most of my problems

test_functions.is_vowel("A") ## brings foward is vowel.

test_functions.calculate_tip(100) ## brings foward tip.

import functions_excercise as fe ## brings foward letter grade
print(fe.get_letter_grade(80))


import itertools  
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

len(list(itertools.product('ABC', '123')))

# How many different combinations are there of 2 letters from "abcd"?

len(list(itertools.combinations('ABCD', 2)))

# How many different permutations are there of 2 letters from "abcd"?

len(list(itertools.permutations('ABCD', 2)))

import json 

profiles = json.load(open('profiles.json')) ## makes the json file a variable for use

print(profiles)

# Total number of users
print(f"The total number of users is {len(profiles)}")

# Number of active users
active_accounts = [accnt for accnt in profiles if accnt['isActive']]
print(f"The total number of active accounts is {len(active_accounts)}")

# Number of inactive users
inactive_accounts = len(profiles)- len(active_accounts)
print(f"The total amount of inactive account is {inactive_accounts}")

print(profiles[0])

# Grand total of balances for all users
bal_list = []
for accnt in profiles:
    bal_list.append(float(accnt['balance'][1:].replace(',','')))
total_balances = sum(bal_list)
print(f'Total balance in users: ${total_balances}')

# Average balance per user
avg_balance=total_balances/len(profiles)
print(f"The average user balance is {avg_balance:.6}")

# User with the lowest balance
min_bal_usr = [accnt for accnt in profiles if float(accnt['balance'][1:].replace(',','')) == min(bal_list)][0] ## [1:] drops the $ and i replace the comma to make a float
print('User with minimum balance is ', min_bal_usr['name'])

# user with the highest balance
max_user = [accnt for accnt in profiles if float(accnt['balance'][1:].replace(',','')) == max(bal_list)][0]
print(f'User with maximum account balance is', max_user['name']) 

# Most common favorite fruit