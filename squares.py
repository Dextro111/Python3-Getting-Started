squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

name = "john"

age = 34
if (age <= 4):
    amount = "Free"
elif ( (age > 4) and (age < 18)):
    amount = 5
elif (age > 18):
    amount = 10

print("The Cost Of Admission is $" + str(amount) + ".")

import sys

num = 1

if num == 1:  
    sys.exit()