# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:


def even_num():
    result = []
    for i in range(1000, 3001):
        digit = str(i)
        if (
            int(digit[0]) % 2 == 0
            and int(digit[1]) % 2 == 0
            and int(digit[2]) % 2 == 0
            and int(digit[3]) % 2 == 0
        ):
            result.append(digit)
    print(",".join(result))


even_num()
