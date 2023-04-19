# Question:
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

inp_str = input("Enter:")
str_list = inp_str.split(",")
odd_list = []
for i in str_list:
    if int(i) % 2 != 0:
        odd_list.append(int(i))
square_list = [str(i * i) for i in odd_list]
print(",".join(square_list))
