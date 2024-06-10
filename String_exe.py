print("Welcome To All Python String Exercises (Answer Displayed)")    # Printing A MSG (INLINE COMMENT)

# Assigning A string To A Variable and Printing it (BLOCK COMMENT)

msg_info = "An Informative Message Regarding The User Of This System"
print(msg_info)

print("#1")

print(len("HOLA! HW U DO"))

#   String Concatenation
string1 = "abra"
string2 = "cadabra"
string3 = "cowabunga"
magic_string = string1 + string2
tmnt_string = string1 + " " + string3
print(magic_string)
print(tmnt_string)

word = "goal"
word = "sh" + word[1:]
print(word)
    # String Slicing

z_str = "bazinga"
print(z_str[2:6])
    
    # Strings Lower And Upper
any_name = " Dwayne 'THE ROCK' Johnson"
print(any_name.lower())
print(any_name.upper())
print(any_name[2:19])
print(any_name.strip())
print(any_name.startswith("DW"))
print(any_name.endswith("son"))

print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honeybadger".lower())

print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honeybadger".upper())
    
    # String WhiteSpace Strip

string1 = "    Filet Mignon"
string2 = "Brisket    "
string3 = "   Cheeseburger    "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())
    
    # Startswith and Endswith Method
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

print(string1.lower().startswith("be"))
print(string2.lower().startswith("be"))
print(string3.lower().startswith("be"))
print(string4.strip().lower().startswith("be"))

    # Taking Users Input
prompt = "Hey, Whats Poppin yo! "
user_input = input(prompt)
print("You Said: ", user_input)

response = input("Who Made You Angry? ")
answer_response = response.upper()
print("So It Was ...", answer_response)

user_input = input("What Should I Call U bro? ")
response = user_input.upper()
numb_response = len(response)
print("Guess u go by " , response)
print("You Inputted", numb_response , "Characters")

    # Usage Of F string
weight = 0.2
animal = "newt"

print(f"{weight} kg is the weight of the {animal}")
print(str(weight)+ " kg is the weight of the" ,animal)
print("{} kg is the weight of the {}".format(weight, animal))

    # Usage Of Find String
print("AAA".find("a"))

