# Largest Number
arr = [2, 1, 33, 234, 233, 3223, 24, 24, 23, 213, 4]

maxi = -9 * 10 ** 7
for i in arr:
    if i > maxi:
        maxi = i
print(maxi)
