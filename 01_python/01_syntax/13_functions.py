def greeter(x: str) -> None:
    print(f"Zola {x}")


y = input("Enter your name :")
greeter(y)


# function for caluculating Body Mass Index
def bmi(w: int, h: float) -> float:
    return w / (h * h)


a = int(input("Enter your weight in KG :"))
b = float(input("Enter your height in m :"))
c = bmi(a, b)

if c < 18.5:
    print(f"{y} is underweight")
elif c < 25:
    print(f"{y} is normal weight")
else:
    print(f"{y} is overweight")
