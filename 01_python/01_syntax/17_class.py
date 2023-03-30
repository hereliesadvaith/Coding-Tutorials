"""
Class:
------
`Class` are just like a building blueprint, they provide you with the
specifications of how to construct a building. It is upto you when and
how you build the building.

Instance:
---------
When you actually construct a building out of the blueprint, it is called as
an `Instance` or `Object` of the class. So, both are related but essential
different terminology.

Class = Blueprint, Instance = Building

Methods:
--------
These are just normal functions, but defined to alter the behavior of your instance or class.
Since they are tied to a class, they are called as methods. Their behavior is dependent on
the structure you define in the class.

When to use Class:
------------------
Use classes only when you need `Structure` and `Behavior` together.

If you only need structure, then choose from any existing data structures such as
list, tuple, dictionary, queue, etc. Just need a behavior? Then just create a function
that transforms your data.

"""


class Someclass:
    pass


print(Someclass)


class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.fn = first_name
        self.ln = last_name

    def __repr__(self) -> str:
        return '<class "Person">'

    def __str__(self) -> str:
        return f"Person: {self.fn} {self.ln}"

    def greet(self) -> None:
        print(f"{self.fn} says hello")


# instance or object of class Person

p1 = Person("Peter", "Griffin")
p2 = Person("Lois", "Griffin")

print(p1)
print(p1.fn)

# Both are different instances of same class at different memmory locations

print(f"p1 is located at memmory address: {hex(id(p1))}")
print(f"p2 is located at memmory address: {hex(id(p2))}")

print(p1.__str__())

p1.greet()
