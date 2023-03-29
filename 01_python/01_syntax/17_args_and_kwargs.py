"""
Variable & Keyword Arguments:
-----------------------------

What happens if we don't know before hand how many arguments we are
going to receive? We can handle this situation by using variable &
keyword arguments syntax.

Info:
-----
We will first look at unpacking first.
"""

from typing import Any

# -----------------unpacking------------------
fname, lname = ("Louis", "Meg")
print(fname)

x, *rest = ["kevin", "peter", "louis", "meg"]
print(rest)

specs = {"type": "dynamic", "optional": "static typing", "found": "everywhere"}
lang = {"name": "python", **specs}
print(lang)


def unknown_friends(*args: str) -> None:
    # Accepts and prints variable argument
    # Variable args are always packed as tuples

    for x in args:
        print(x)


unknown_friends("Cece", "Roko", "Chiko", "Niko", "Jake", "Mario")


def unknown_product(**kwargs: Any) -> None:
    # Accepts and prints variable keyword argument
    # Keyword args are always packed as dictionary

    for key, value in kwargs.items():
        print(f"{key}:{value}")


unknown_product(name="pizza", price=3.99, topping="olives", extra_cheese=True)


def invoice(product: str, *args, **kwargs):
    print(product)
    print(args)
    print(kwargs)


invoice(
    "sneakers",
    "black",
    "white",
    brand="Nike",
    category="Air Jordans",
    price=899.99,
    in_stock=False,
)
