# Question: Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input

number = int(input("Number: "))


def factorial(number):
    output = 1
    while number > 1:
        output *= number
        number -= 1
    return output


# or you can use recurssion of function but recurssion is slower than looping
def factorial1(number):
    if number == 1:
        return 1
    return number * factorial1(number - 1)


print(factorial(number))
