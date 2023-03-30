"""
Decorators:
-----------
They are used to implement particular behavior for our classes.

Summary:
--------
1. property - Acts like a instance variable, no need to call like function.
2. static method - Directly called from the class.
3. class method - Returns a new instance of the class.
4. getter & setter - Used for `Data Encapsulation`.

Info:
-----
We can mark the class as `final` so that no other class can subclass it.

"""

from __future__ import annotations
from enum import Enum, auto
from datetime import datetime
from typing import final


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    @property  # act like self.fname
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"


p1 = Person("Pam", "Bleesley")
print(p1)
print(p1.fullname)  # can call like this


@final
class Staff(Person):
    def __init__(self, fname: str, lname: str, staff_id: int, role: Role) -> None:
        super().__init__(fname, lname)
        self.staff_id = staff_id
        self.is_staff = True
        self.role = role
        # Private member
        self.__date_joined = datetime.now().strftime("%B %d, %Y")
        # Dynamically create and assign instance values
        match role:
            case Role.ASSOCIATE:
                # Private member
                self.__salary: float = 15
            case Role.SUPERVISOR:
                self.__salary = 20
            case Role.MANAGER:
                self.__salary = 25

    def __str__(self) -> str:
        # can add property of parent class without calling it. ie: fullname
        return f"Staff => Name: {self.fullname} ID: {self.staff_id}"

    @classmethod
    def new(cls, person: Person, staff_id: int, role: Role) -> Staff:
        return cls(person.fname, person.lname, staff_id, role)

    # Getter
    @property
    def joined_on(self) -> str:
        return f"{self.__date_joined}"

    @staticmethod
    def describe() -> None:
        # Describes what the class does
        print("Class to create a staff member")

    @property
    def salary(self) -> float:
        return self.__salary

    # Setter
    @salary.setter
    def salary(self, amt: float) -> None:
        if self.role == Role.ASSOCIATE and amt < 15:
            print("Error")
        elif self.role == Role.SUPERVISOR and amt < 20:
            print("Error")
        elif self.role == Role.MANAGER and amt < 25:
            print("Error")
        else:
            self.__salary = amt
            print(f"{self.fullname} now has a salary of {amt}")


Staff.describe()
p2 = Person("Peter", "Griffin")
s1 = Staff("Chris", "Griffin", 7890, Role.ASSOCIATE)
s2 = Staff.new(p1, 7654, Role.MANAGER)

print(p1)
print(p1.fullname)
print(s1)
print(s1.joined_on)
print(s2)
print(s1.salary)

s1.salary = 17
