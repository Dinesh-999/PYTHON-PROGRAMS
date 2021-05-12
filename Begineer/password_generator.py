# random password generator
#

import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "!@#$%&*()-+"

upper, lower, num, symb = True, True, True, False
# above line is used to involve the characters in password,
# if u make false it will not involve

all = ''

if upper:
    all += uppercase

if lower:
    all += lowercase

if num:
    all += numbers

if symb:
    all += symbols

length = 15  # password length
amount = 10  # how many passwords should print

# seed = "Dinesh"  # if seed is used same passwords will generate every time
# random.seed(seed)

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

"""
# create a test.txt file
# this code is to write the passwords in test.txt file

with open("test.txt", "a") as f:
    for i in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
        f.write(password + "\n")
"""
