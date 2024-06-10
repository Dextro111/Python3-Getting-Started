alien_color = "red"

if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
elif alien_color == "red":
    points = 15

print("You Just Earned" , points , "Points")

#   Creating more aliens using 
aliens = []

for alien_num in range(20):
    new_alien = {"color": "green", "points": 5, "speed":"slow"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
print("...")