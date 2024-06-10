alien_0 = {'color': "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["size"] = "large"
alien_0["speed"] = "medium"

print("Original X-Position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0["speed"] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

del alien_0["size"]
print(alien_0)

#   Favourite Languuages 
print("\n")
fav_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "javascript",
    "phil": "python",
}
print("Edwards Fav Language Is " + fav_languages["edward"])

    #   person_info
print("\n")

person = {"first_name": "David",
          "last_name": "Umoh",
          "age": "17_yrs",
          "city": "Port_Harcourt"
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

#   Looping through Dictionary
for name in set(fav_languages.values()):
    print("\nName: " + name)

alien_1 = {"color": "green", "points": 5}
alien_2 = {"color": "yellow", "points": 10}
alien_3 = {"color": "yellow", "points": 15}

aliens = [alien_0,alien_1,alien_2,alien_3]

for alien in aliens:
    print(alien)


































