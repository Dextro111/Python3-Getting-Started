Result = {}

# Setting A flag To Show Its Active
career_poll = True

while career_poll:
    # Prompt for The Persons Name And Future Career.
    name = input("What Is Your Name? ")
    career = input("What Would You Like To Be In Future? ")

    #store the career in the dictionary"
    Result[name] = career

    #CheckIf Anyone Else Would Participate.
    repeat = input("Would You Like to let Another Respond? (yes/ no) ")
    if repeat == "no":
        career_poll = False

# Career Poll is Complete. Show The Results.
print("\n------ Poll Results ------")

# Use A For Loop to print out the key value pairs in the dictionary

for name, career in Result.items():
    print(name + " would like to be a " + career + ".")