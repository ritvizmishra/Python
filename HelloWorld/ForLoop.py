# For Loop

# on string
for item in "Ritviz":
    print(item.upper())

# on list
for item in ["Ritviz", "Mishra", "19/BCS/128", "Gautam Buddha University"]:
    print(item)

# on range
for item in range(1, 30, 3):
    print(item)

# Shopping List
bill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
price = 0
for i in bill:
    price += i
print(f"Total money spent = ${price}")
