# Create a program which is password protected, and wont open unless the correct 
# user and password is given.
# For extra credit, have the user and password in a seperate .txt file.
# For even more extra credit, break into your own program :)

def lock_switch(state):
  if(state):
    return False
  return True

def lock_status(state):
  if(not state):
    return "you have opened the safe. may all your dreams come true"
  return "the safe is locked. get the fahk outta heeeeaaah kid"

lock = True

username = open("easy_challenge_5_username.txt", "r")
password = open("easy_challenge_5_password.txt", "r")

print("+--------------------------+")
print("| UNHACKABLE SAFE HA HA HA |")
print("+--------------------------+")
username_input = raw_input("username: > ")
password_input = raw_input("password: > ")


print(username)
print(password)

if(username == username_input and password == password_input):
  if(lock):
    lock = lock_switch(lock)
  print(lock_status(lock))
else:
  print(lock_status(lock))

username.close()
password.close()
