    # Challenge: Convert Temperatures (F and C)
Digit = True

while Digit:
    F = float(input("\nEnter A Temperature In Degrees F: "))
    def convert_far_to_cel(F):
        """Converts Farenheit To Celsius"""
        C_temperature = (F - 32) * 5/9
        C_statement = f"{F:.0f} degrees F = {C_temperature:.2f} degrees C"
        return C_statement
    num = convert_far_to_cel(F)
    print(num)

    C = float(input("Enter A Temperature In Degrees C: "))
    def convert_cel_to_far(C):
        """Converts Celsius To Farenheit"""
        F_temperature = C * 9/5 + 32
        F_statement = f"{C:.0f} degrees C = {F_temperature:.2f} degrees F"
        return F_statement
    num1 = convert_cel_to_far(C)
    print(num1)
    
    Exit = input("\nDo You Want To End The Program(y/n): ")
    
    if Exit == "y":
        Digit = False
    
