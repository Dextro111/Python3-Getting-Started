num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

num = 175e+3
print(num)

test = "12"
string_num = int(test) * 3
print(string_num)
string_num = float(test) * 3
print(string_num)

num = input("Enter a number to be doubled: ")
doubled_num = float(num)* 2
print(doubled_num)

numb = float(input("Enter A Number: "))
rounded_number = round(numb, 2)
absolute_number = abs(numb)

print(f"{numb} Rounded To 2 Decimal Places Is {rounded_number}")

print(f"The Absolute Value Of {numb} is {absolute_number}")

num_1 = float(input("Enter A Number: "))
num_2 = float(input("Enter Another Number: "))
evaluation = (num_1 - num2).is_integer()

print(f"The Difference Between {num_1} And {num_2} Is An Integer? {evaluation}!")

result = 3 ** .125
print(f"{result:.3f}")

result = 150000
print(f"{result:,.2f}")

result_1 = 2 / 10
print(f"{result_1:.0%}")