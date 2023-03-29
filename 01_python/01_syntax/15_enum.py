from enum import Enum, auto


class Pizzasize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12


print(f"One order for {Pizzasize.SMALL.value} inch pizza")


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


print(Role.MANAGER.value)
