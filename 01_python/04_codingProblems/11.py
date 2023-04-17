# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

inp_str = input("Binary Numbers:").strip(",")  # to remove trailing commas and spaces
str_list = inp_str.split(",")
result = []
for i in str_list:
    ind_i = len(i) - 1
    value = 0
    for j in i:
        value += int(j) * (2**ind_i)
        ind_i -= 1
    # check if it's divsible by 5 then add to list
    if value % 5 == 0:
        result.append(value)
my_string = ",".join(str(x) for x in result)
print(my_string)

# or you can just use built-in binary function

result2 = []
items = [x for x in input().split(",")]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        result2.append(p)

my_string2 = ",".join(str(x) for x in result)
print(my_string2)
