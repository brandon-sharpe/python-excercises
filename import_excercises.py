import test_functions

test_functions.is_vowel("A")

test_functions.calculate_tip(100)

import functions_excercise as fe
print(fe.get_letter_grade(80))


import itertools

list(itertools.combinations('ABC123', 5))

list(itertools.combinations('ABCD', 3))

list(itertools.permutations('ABCD', 2))

import json

profiles = json.load(open('profiles.json'))

print(profiles)


active_accounts = [accnt for accnt in profiles if accnt['isActive']]
print(len(active_accounts))

print(profiles[0])

balances=[]
for accnt in profiles:
    balances.appen(profiles['balance'])
bal_list = []
for accnt in profiles:
    bal_list.append(float(accnt['balance'][1:].replace(',','')))
total_balances = sum(bal_list)
print(f'Total balance in users: ${total_balances}')