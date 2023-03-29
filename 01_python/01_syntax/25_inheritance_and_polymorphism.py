"""
Inheritance:
------------
All species inherit a lot from their parents, may be they have same eyes as
their mother but different voice all together.

Python classes are no different, we can inherit from classes and make them share
common functionality. At the same time we can dynamically add other features and
functionality as well.

Polymorphism:
-------------
Suppose there are two children, one want's to speak in Marathi, other want's to
speak in Sanskrit. This is possible using polymorphism! It's just creating the same
methods but with different behavior.
"""


class Animal:
    def __init__(self, name: str, age: int, num_legs: int) -> None:
        # Create and initialize instance variables
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Num_legs: {self.num_legs}"

    def talk(self) -> None:
        print(f"{self.name} can't talk yet")


class Dog(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        # Take the common features and pass to the parent(super) class
        super().__init__(name, age, num_legs)
        # Define custom instance variables
        self.breed = breed
        self.type = "Dog"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    # We alter the talk method and make it say woff adding polymorphic behavior

    def talk(self) -> None:
        print(f"{self.name} says wooof")

    def sniff(self, item: str) -> None:
        print(f"{self.name} is sniffing out {item}")


a1 = Animal("Liger", 12, 4)
print(a1)
a1.talk()


d1 = Dog("Brian", 8, 4, "Dobberman")
print(d1)
d1.talk()
d1.sniff("ball")

# .................................................................


class Cat(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        # Take the common features and pass to the parent(super) class
        super().__init__(name, age, num_legs)
        # Define custom instance variables
        self.breed = breed
        self.type = "Cat"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    def talk(self) -> None:
        print(f"{self.name} says meowww..")


c1 = Cat("Snowbell", 4, 4, "Persian cat")
print(c1)
c1.talk()

# ......................................................................

print(isinstance(d1, Animal))
