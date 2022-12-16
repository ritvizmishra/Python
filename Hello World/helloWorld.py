import math

# print statement
print("Ritviz Mishra says Hello to the World!")

# declare without types
name = "Ritviz Mishra"
rollNumber = 128
currentGPA = 8.08
print(name, rollNumber, currentGPA)

# taking input
user = input("What is your name? ")
print("Hi, " + user)
print(user + " likes books.")

# type casting
birthYear = input("What is your birth year? ")
age = 2022 - int(birthYear)
print("You are ", age, " years old.")

# formatted string
first_name = "Ritviz"
last_name = "Mishra"
message = f"{first_name} [{last_name}] is a programmer."
print(message)
print("is" in message)
print(len(message))
print(message.upper())

a = 2.9
# Arithmetic Operators
print(a // 2)

# math functions
print(math.ceil(a))

