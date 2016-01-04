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
    return "you have opened the safe with the proper credentials.\n\t- may all your dreams come true"
  return "the safe is locked. get the fahk outta heeeeaaah kid"


# main
lock = True

# with open("easy_challenge_5_username.txt", "r") as file:
#   userfile_content = file.readlines()
# file.close()
# with open("easy_challenge_5_password.txt", "r") as file:
#   passfile_content = file.readlines()

# compared with the method above, this method leaves the file open which is 
# considered bad practice but ultimately does not matter for small files by 
# some. unsure of who to believe..
userfile_lines = [line.rstrip('\n') for line in open("easy_challenge_5_username.txt")]
passfile_lines = [line.rstrip('\n') for line in open("easy_challenge_5_username.txt")]

username = userfile_lines[0]
password = passfile_lines[0]

print("+--------------------------+")
print("| UNHACKABLE SAFE HA HA HA |")
print("+--------------------------+")
username_input = raw_input("username: > ")
password_input = raw_input("password: > ")


print(username_input+", "+username)
print(password_input+", "+password)

if(username == username_input and password == password_input):
  if(lock):
    lock = lock_switch(lock)
  print(lock_status(lock))
else:
  print(lock_status(lock))

