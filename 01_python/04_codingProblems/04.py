# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate
# a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

# Solution:

serial = int(input("How many numbers do you wanna add:"))
num_list: list = []

for i in range(0, serial):
    num = int(input(f"{i + 1} Number:"))
    num_list.append(str(num))

print(num_list)
print(tuple(num_list))

# or
values = input()
l = values.split(",")
t = tuple(l)
print(l)
print(t)
