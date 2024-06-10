prompt = "\nTell Me Something, And I Will Repeat It Back To U:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
