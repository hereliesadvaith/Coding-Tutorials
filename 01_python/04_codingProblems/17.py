# Question:
# Write a program that computes the net amount of a bank account based a transaction log
# from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

output = 0
while True:
    inp_str = input()
    if inp_str:
        str_list = inp_str.split(" ")
        if str_list[0] == "D":
            output += int(str_list[1])
        elif str_list[0] == "W":
            output -= int(str_list[1])
        else:
            print("wrong input")
    # to get out of function press enter twice
    else:
        break
print(output)
