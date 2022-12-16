# If - Else Conditions
age = input("What is your age? ")

if 18 <= int(age) <= 65:
    print("You can vote.")
elif int(age) > 65:
    print("You are not eligible to vote.")
else:
    print("not you!")

# Solution to the question
house_Price = 1000000
good_Credit = False

if good_Credit:
    print(f"Down payment is ${ house_Price * 0.1}")
else:
    print(f"Down payment is ${ house_Price * 0.2}")

# solution temperature
temperature = input("What is the current temperature? ")

if int(temperature) >= 20:
    print("it's hot.")
elif 0 <= int(temperature) < 20:
    print("it's cold.")
else:
    print("it's very cold")

# name eg.
name = input("What is your name? ")

if len(name) < 3:
    print("Should be at least 3 chars long")
elif len(name) > 50:
    print("maximum name length shall be 50 chars")
else:
    print("noice name")

# Weight Convertor
weight = input("Enter your weight: ")
unit = input("Which unit you want to convert it into: ")

if unit.lower() == 'k':
    print("Your weight in kgs is: ", int(weight) / 2.205)
elif unit.lower() == 'l':
    print("Your weight in lbs is: ", int(weight) * 2.205)
else:
    print("Invalid unit selected.")


