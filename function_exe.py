def multiply(x, y ):
    """Returns The product of two numbers x and y."""
    product = x * y
    return product

num = multiply(2,4)
print(num)

def cube(a):
    """Returns The Number Raised To Power Three."""
    power_3 = a ** 3
    return power_3
val = cube(3)
print(val)

def greet(name="Dextro_Blaze" ):
    """Displays A Hello Greeting"""
    text = f"Hello {name}!"
    return text
result = greet()
print(result)

    #   While Loop
try:
    num = float(input("Enter A Positive Number!"))
except ValueError:
    print("This Is Not An Integer")
 
while num <= 0:
    print("That Is Not A Positive Number! U Stupid!!!")
    num = float(input("U Better Enter A Positive Number.Fool! : "))

    #   For Loop
for letter in "Python":
    print(letter)

for n in range(4):
    print("python")

for n in range(10, 20):
    print(n * n)

amount = float(input("Enter an Amount: "))

for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:.2f} each")

for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")

for integer in range(2, 10):
    print(integer, "used Range")

n = 2
while n < 10:
    print(n, "without Range")
    n = n + 1

numb = int(input("Enter a number to be DOUBLED: "))
def doubles(numb):
    doub_num = numb * 2
    return doub_num

for val in range(5):
    print(doubles(numb))
    numb = numb * 2

