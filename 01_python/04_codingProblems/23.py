# Question:

# Please write a program to print some Python built-in functions documents,
# such as abs(), int(), raw_input()
# And add document for your own function
# Hints:
# The built-in document method is __doc__

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    "The function takes a number as input and returns it's square"
    return num * num


print(square.__doc__)
print(square(11))
