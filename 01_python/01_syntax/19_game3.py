from random import randint
from typing import Final

Character = dict[str, str | int]

hero_life = 0
villain_life = 0


def inc_hero_life(life: int):

    global hero_life
    hero_life += life


def dec_hero_life(life: int):

    global hero_life
    hero_life -= life


def inc_villain_life(life: int):

    global villain_life
    villain_life += life


def dec_villain_life(life: int):

    global villain_life
    villain_life -= life


def get_all_superheros() -> list[Character]:

    IRONMAN: Final[Character] = {"name": "Ironman", "attpwr": 250, "life": 1000}
    BLACKWIDOW: Final[Character] = {"name": "Blackwidow", "attpwr": 180, "life": 800}
    SPIDERMAN: Final[Character] = {"name": "Spiderman", "attpwr": 190, "life": 900}
    HULK: Final[Character] = {"name": "Hulk", "attpwr": 300, "life": 1100}

    superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return superheros


def get_superhero(index: int) -> Character | None:

    superheros = get_all_superheros()
    if index < len(superheros):
        return superheros[index]
    else:
        return None


def get_all_villains():

    THANOS: Final[Character] = {"name": "Thanos", "attpwr": 400, "life": 1500}
    REDSKULL: Final[Character] = {"name": "Redskull", "attpwr": 300, "life": 800}
    PROXIMA: Final[Character] = {"name": "Proxima", "attpwr": 320, "life": 800}

    villains: list[Character] = [THANOS, REDSKULL, PROXIMA]
    return villains


def get_villain(index):

    villains = get_all_villains()
    if index < len(villains):
        return villains[index]
    else:
        return None


def attack_num():

    for attack_num in range(3):
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)

        current_hero = get_superhero(hero_index)
        current_villain = get_villain(villain_index)

        if current_hero and current_villain:
            simulate_attack(attack_num, current_hero, current_villain)

        else:
            print("Error.... No one is fighting")


def simulate_attack(attack_num: int, hero: Character, villain: Character):

    inc_hero_life(int(hero["life"]))
    inc_villain_life(int(villain["life"]))
    dec_hero_life(int(villain["attpwr"]))
    dec_villain_life(int(hero["attpwr"]))
    print(
        f"Attack: {attack_num + 1} ==> {hero['name']} and {villain['name']} are fighting"
    )


def win_or_lose():

    print("=" * 50)

    if hero_life >= villain_life:
        print("Avengers Won")
    else:
        print("Avengers Dead")


def main():

    attack_num()
    win_or_lose()


main()
