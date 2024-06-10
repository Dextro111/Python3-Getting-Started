Rivers = {"Nile": "Egypt", "Missisipi": "United States", "Amazon": "Peru-Brazil"}

for river,location in Rivers.items():
    print(f"The {river} Runs Through {location}")

print("\n")

for river in Rivers.keys():
    print(f"{river} Is A Major River In The World")

print("\n")

for location in Rivers.values():
    print(f"{location} Contains One Of The Major Rivers In The World")