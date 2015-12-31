# write a program that can encrypt texts with an alphabetical caesar cipher. 
# This cipher can ignore numbers, symbols, and whitespace.
# For extra credit, add a "decrypt" function to your program!

import string


def encrypt(letter, shift):
  return (alpha.index(letter) + shift) % 26

def decrypt(letter, shift):
  return (alpha.index(letter) - shift) % 26


alpha = list(string.ascii_lowercase)
s = "ancient chinese secret"
x = ""
y = ""
user_string = raw_input("\nenter a message: > ")
user_shift = int(raw_input("enter shift amount: > "))

# encrypt
for i in range(len(user_string)):
  if user_string[i] == " ":
    x += " " 
    continue
  secret = alpha[encrypt(user_string[i], user_shift)] 
  x += secret
# print("original message:   "+s)
print("encrypted message:  "+x)

# decrypt
for i in range(len(x)):
  if x[i] == " ":
    y += " "
    continue
  known = alpha[decrypt(x[i], user_shift)]
  y += known
print("decrypted message:  "+y+"\n")
