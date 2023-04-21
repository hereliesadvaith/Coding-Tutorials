# Question
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from
# current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example:
# If the following  are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2, 0

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:
import math

inp_list = []
while True:
    inp_str = input("Enter:")
    if inp_str:
        inp_list.append(inp_str.split(" "))
    else:
        break
x = 0
y = 0
for i in inp_list:
    match i[0].lower():
        case "up":
            y += int(i[1])
        case "down":
            y -= int(i[1])
        case "right":
            x += int(i[1])
        case "left":
            x -= int(i[1])
print(
    f"""
Current Position: {x},{y}
Displacement: {round(math.sqrt(x ** 2 + y ** 2))}
"""
)
