# Question:
# Write a program that accepts a sentence and calculate the number of
# upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

inp_str = input("Enter:")
upr_case = ""
low_case = ""

for i in inp_str:
    if i.isupper():
        upr_case += i
    if i.islower():
        low_case += i

print(
    f"""
    UPPER CASE {len(upr_case)}
    LOWER CASE {len(low_case)}
"""
)
