# create a program that will ask the users name, age, and username. have it 
# tell them the information back, in the format:
# your name is (blank), you are (blank) years old, and your username is (blank)
# for extra credit, have the program log this information in a file to be 
# accessed later.

file = open("easy_challenge_1_save.txt", "w")

name = raw_input("enter your name: ")
age = raw_input("enter your age: ")
username = raw_input("enter your username: ")

print("\nwriting data to file...")
file.write(name+"\n")
file.write(age+"\n")
file.write(username+"\n")
print("completed\n\n")

print("your name is "+name+", you are "+age+" years old, and your username is "+username)

file.close()