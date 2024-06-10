pizza_toppings = []
prompt = "Enter A New Pizza Topping: "
prompt += "\nEnter 'quit' to exit the Program. "

active = True
while active:
    response = input(prompt)
    pizza_toppings.append(response)

    if response == "quit":
        active = False
    else:
        print(f"You Added {response} To Your Pizza.")

print("Toppings In Your Pizza Includes:" , pizza_toppings[:])

