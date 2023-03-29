def greeter2(y: str) -> None:
    print(f"Zola {y}")


y = input("Enter your name :")
greeter2(y)


def bmi(w: int, h: float) -> float:
    return w / (h * h)


a = int(input("Enter your weight in KG :"))
b = float(input("Enter your height in m :"))
c = bmi(a, b)
if c < 18.5:
    print("You are underweight")
elif c < 25:
    print("You are normal weight")
else:
    print("You are overweight")
