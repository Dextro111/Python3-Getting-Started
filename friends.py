Class_Boys = ["Chimkoski", "Marve", "Pere", "Solo", "J_monie", "Umoh", "Austin"]
names = ["Marve", "Pere" , "Solo" , "Austin", "Chimkoski"]

for boys in Class_Boys:
    if boys in names:
        print(boys , "Attended The Main FutBall Match")
    else:
        print(boys, ", Where Were You, Bro!")

print("\n")

print(names[0: 4])

cool_name = names[:]
print("Cool Dudes")
print(cool_name)

print("Marve" in names)     # Truth Value 

print("\n")
if "umoh" not in names:
    print("Sorry bro")

if 'Marve' in names:
    print("Marvellous D")
if 'Solo' in names:
    print("Solomon E")
if "Goodie" in names:
    print("Goodluck I")

print("\n")

cars_models = ["mercedes benz" , "rolls Royce" , "buggati", "Ferrari"]
for cars in cars_models[0:3]:
    print("I Would Love To own a ".title() , cars.upper())
