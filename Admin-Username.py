    #   Hello Messages To The Admin
usernames = ["Dextro", "Marve", "Solo", "J_Monie", "admin"]

if usernames == []:
    print("We Need To Find Some Valuable Users!")
else:
    for names in usernames:
        if names == "admin":
            print("Hello Admin, Your Welcome, Would U Wanna See The Status Report?")
        elif usernames != "admin":
            print("Hello" ,names , ", Your Welcome!")
print("\n")

    # Checking Usernames
current_users = ["Ami","Lera","Bliss","Umoh","Goodie"]
new_users = ["Ronald", "Frankie","AmI","lERA","UMOH" ]

for new_user in new_users:
    if new_user.title() in current_users:
        print("Sorry", new_user.title(), "U Need To Enter A New UserName!")
    else: 
        print(new_user,"This UserName Is Available!")