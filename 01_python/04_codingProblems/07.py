# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the question,
# it should be assumed to be a console input in a comma-separated form.

# Solution:

inp_str = input("Enter Row, Col:")
str_list = inp_str.split(",")
row, col = int(str_list[0]), int(str_list[1])
output = [[row * col for col in range(0, col)] for row in range(0, row)]
print(output)
