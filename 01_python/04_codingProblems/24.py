# Question:
# Define a class, which have a class parameter and have a same instance parameter.

# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later

# Solution:

class Person():
    # define class parameter "name"
    name = "Person"
    def __init__(self, name) -> None:
        # self.name is instance parameter
        self.name = name

peter = Person("Peter")
print("%s name is %s" %(Person.name, peter.name))