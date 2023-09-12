print("hello world !")

# different values for multiple variables
x, y, z = "orange", "apple", "mango"

# same value for multiple variables
x = y = z = "orange"

# unpack collection
fruits = ["orange", "apple", "mango"]
x , y, z = fruits
print(x) # "orange"

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # Python is awesome
print(x + y + z) # Pythonisawesome

x = 5
y = "7"
print(x, y) # 5 7