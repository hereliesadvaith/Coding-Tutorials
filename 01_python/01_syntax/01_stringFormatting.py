# String concatenation (aka how to put strings together)

name = "Advaith"
age = "23"

print(f"{name} is {age} years old")

customer: str = input("Customer:")
count: int = int(input("Qty:"))
pizza_size: int = int(input("Size in Inches:"))
toppings: str = input("Topping:")
price: float = 40

order_details: str = f"""
Received order from: {customer}
Size: {pizza_size} inches
Topping: {toppings}
Bill Amount: {price}
"""
print(order_details)
