class Character:

    # Defines class
    def __init__(self, name: str, att_pwr: int, life: int) -> None:
        # Creates an instance of character
        self.name = name
        self.att_pwr = att_pwr
        self.life = life

    def __repr__(self) -> str:
        return "<class 'Character'>"

    def __str__(self) -> str:
        return f"Name: {self.name}, Att_Pwr: {self.att_pwr}, Life: {self.life}"


villain1 = Character("Thanos", 500, 1500)

# Using key value pairs
villain2 = Character(name="Redskull", life=800, att_pwr=300)

hero1 = Character("Ironman", 300, 900)
hero2 = Character("Blackwidow", 180, 500)
hero3 = Character("Spiderman", 230, 800)


print(villain1)
print(villain2)
