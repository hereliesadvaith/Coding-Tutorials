from __future__ import annotations


class Box:
    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self) -> int:
        return self.side_a * self.side_b

    def __repr__(self) -> str:
        return "<class 'Box'>"

    def __str__(self) -> str:
        return f"Box => Side A: {self.side_a}, Side B: {self.side_b}"

    def __contains__(self, num: object) -> bool:
        if not isinstance(num, int):
            raise NotImplementedError

        return num in [self.side_a, self.side_b]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Box):
            raise NotImplemented
        return (self.side_a == other.side_a) and (self.side_b == other.side_b)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area < other.area

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area <= other.area

    def __add__(self, other: object) -> int:
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area + other.area

    def __truediv__(self, other: object) -> float:
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area / other.area

    def __floordiv__(self, other: object) -> int:
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area // other.area


b1 = Box(3, 5)
print(4 in b1)
b0 = Box(3, 5)
print(b1 == b0)
print(b1 < b0)
print(b1 <= b0)
# also
print(b1 > b0)
print(b1 + b0)
print(b1 / b0)
