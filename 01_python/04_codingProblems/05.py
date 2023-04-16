# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters


class InOutString:
    def __init__(self) -> None:
        # variable
        self.string = None

    def getString(self):
        self.string = input("Enter :")
        print(self.string)

    def printString(self):
        print(self.string.upper())


string_1 = InOutString()
string_1.getString()
string_1.printString()
