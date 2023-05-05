from sqlalchemy import ForeignKey, create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("postgresql://advaith:pswd@localhost:5432/mydb")


class Person(Base):  # type: ignore
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    f_name = Column("f_name", String)
    l_name = Column("l_name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, f_name, l_name, gender, age):
        self.ssn = ssn
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.age = age

    def __repr__(self) -> str:
        return f"{self.ssn} {self.f_name} {self.l_name} {self.gender} {self.age}"


class Thing(Base):  # type: ignore
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner_id = Column("owner_id", Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner_id):
        self.tid = tid
        self.description = description
        self.owner_id = owner_id

    def __repr__(self) -> str:
        return f"{self.tid} {self.description} {self.owner_id}"


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(323464, "Aswathy", "Advaith", "F", 25)
t1 = Thing(23, "Car", p1.ssn)

session.add(p1)
session.add(t1)
session.commit()
