# Create a random password generator!
# For extra credit, allow the user to specify the amount of passwords to generate.
# For even more extra credit, allow the user to specify the length of the strings 
# he wants to generate!

import random
import string

alpha = list(string.ascii_lowercase)
alpha_test = ["a","b","c","d","e"]


pass_len = int(raw_input("enter password length: > "))
pass_amount = int(raw_input("enter total passwords: > "))
print("\n\n")
# print(alpha)
# print(random.sample(alpha, pass_len))
print(random.sample(alpha_test, pass_len))
print("\n\n")
# print(alpha*pass_len)
# print(random.sample(alpha*pass_len, pass_len))
print(random.sample(alpha_test*pass_len, pass_len))
print("\n\n")
# print(str(alpha*pass_len)+"\n\n")
for i in range(pass_amount):
  print(''.join(random.sample(alpha*pass_len, pass_len)))
