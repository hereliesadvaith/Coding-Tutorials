# Functions under the hood are just objects
# They can be passed to other functions and functions can also return functions
# We can send function to data


from typing import Callable

# Function accepting a function


def good_morning(name: str) -> str:
    return f"Good morning {name}"


def goodbye(name):
    return f"Goodbye {name}"


def universal_greeter(name: str, greeter: Callable[[str], str]):
    msg = greeter(name)
    print(msg)


universal_greeter("Advaith", good_morning)
universal_greeter("Niharika", goodbye)

# Function returning a function


def add_by_5(num: int) -> Callable[[], int]:
    def by_5() -> int:
        return num + 5

    return by_5


sum = add_by_5(6)

print(sum())


# Lambda functions:

zola = lambda name: f"Zola {name}"

universal_greeter("Advaith", zola)
