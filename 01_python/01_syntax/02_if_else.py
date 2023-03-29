name = input("Name:")
age: int = int(input("Age:"))

# check if you are eligible for a driving license.


if age >= 18 and age <= 60:
    print(f"{name} is eligible")
elif age > 60:
    print(f"{name} is too old")
else:
    print(f"{name} is not eligible")
