# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.

# Hints:
# Consider use yield
# yield is a keyword in Python that is used in the context of generator functions to create iterators.
# Generator functions are a type of function in Python that use the yield keyword to return
# a generator object, which can be iterated over using a for loop or the next() function.

# Solution:


def putNumbers(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j


inp_num = int(input("Enter Num:"))
genrator = putNumbers(inp_num)

print(next(genrator))  # output 0
print(next(genrator))  # output 7
# or you can use a for loop
