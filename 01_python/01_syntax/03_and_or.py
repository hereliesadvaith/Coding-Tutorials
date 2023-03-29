planet: str = "Zortan"
age: int = 18

if age >= 16 and planet == "Earth":
    print("You are eligible")
elif age >= 16 or planet == "Zortan":
    print("You are eligible")
else:
    print("You are not eligible")
