planet: str = "Zortan"
age: int = 18

# You don't have to be 16 to get license in planet Zortan. Check your eligiblity.

if age >= 16 and planet == "Earth":
    print("You are eligible")
elif age >= 16 or planet == "Zortan":
    print("You are eligible")
else:
    print("You are not eligible")
