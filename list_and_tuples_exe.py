    # Few Example Of Lists And Its Methods
Cars_Brand = ["honda", "yamaha", "suzuki","toyota","lexus-330", "mercedes"] 
print(Cars_Brand)

print("I Have A " ,Cars_Brand[2].upper())
print(Cars_Brand[-1])

Cars_Brand.append("camry")
Cars_Brand.insert(0, "bmw")

print("\n",Cars_Brand)

del Cars_Brand[3]
Cars_Brand[1] = "mercedes"

old_mercedes = Cars_Brand.pop(-2)
print("Too many ", old_mercedes)
Cars_Brand.remove("yamaha")
print(Cars_Brand)
Cars_Brand.sort()
print(Cars_Brand)
print(len(Cars_Brand))

for cars in Cars_Brand:
    print("I'm gonna buy a ", cars.title())

print("someday".capitalize())

players = ["Chelsea","Mancity","liverpool","Manutd","Arsenal"]
print(players[-3:])