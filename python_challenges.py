    # Challenge: Pick Apart Ur Users Input

user_input = input("Tell Me Your Password: ")
first_letter = user_input[0].capitalize()
print("The First Letter Of Ur Password Is:",first_letter)

    # Challenge: Turn Ur User Into A L33t H4xor

prompt = input("Enter Some text: ")
answer = prompt.replace("a","4")
answer = answer.replace("b", "8")
answer = answer.replace("e", "3")
answer = answer.replace("l", "1")
answer = answer.replace("o", "0")
answer = answer.replace("s", "5")
answer = answer.replace("t", "7")
print(answer)

    # Challenge: Perform Calculations On User Input

first_num = input("Enter A BASE: ")
second_num = input("Enter An EXPONENT: ")
result = float(first_num) ** float(second_num)
print(f"{first_num} To The Power Of {second_num} = {result}")

    # Challenge: Convert Temperatures (F and C)

F = float(input("Enter A Temperature In Degrees F: "))
def convert_far_to_cel(F):
    C_temperature = (F - 32) * 5/9
    C_statement = f"{F:.0f} degrees F = {C_temperature:.2f} degrees C"
    return C_statement
print(convert_far_to_cel(F))

C = float(input("Enter A Temperature In Degrees C: "))
def convert_cel_to_far(C):
    F_temperature = C * 9/5 + 32
    F_statement = f"{C:.0f} degrees C = {F_temperature:.2f} degrees F"
    return F_statement
print(convert_cel_to_far(C))
