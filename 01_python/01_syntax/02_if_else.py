name = input("Name:")
age: int = int(input("Age:"))
if age >= 18 and age <= 60:
    print(f"{name} is eligible")
elif age > 60:
    print(f"{name} is too old")
else:
    print(f"{name} is not eligible")
